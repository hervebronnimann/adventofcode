BEGIN { hit=100; armor["none"]=1; ring["none"]=$1; cost["none"]=0; dam["none"]=0; arm["none"]=0; }
/^Hit:/    { bhit = $2; }
/^Damage:/ { bdam = $2; }
/^Armor:/  { barm = $2; }
/^W / { weapon[$2]=1; cost[$2]=$3; dam[$2]=$4; arm[$2]=0; }
/^A / { armor[$2]=1;  cost[$2]=$3; dam[$2]=0; arm[$2]=$5; }
/^Damage /  { ring[$1 $2]=1; cost[$1 $2]=$3; dam[$1 $2]=$4; arm[$1 $2]=0; }
/^Defense / { ring[$1 $2]=1; cost[$1 $2]=$3; dam[$1 $2]=0; arm[$1 $2]=$5; }
function max(x,y) { return x>y?x:y; }
function win(h,d,a) {
  bh=bhit;
  if (verbose) {
    print "Boss takes "d"-"ba"=" max(1,d-ba) " damage, down to " bh - max(1,d-ba)
    print "Player takes "d"-"ba"=" max(1,d-ba) " damage, down to " bh - max(1,d-ba)
    print "etc."
  } 
  while (1) {
    bh -= max(1,d-barm); if (bh<=0) return 1;
    h -= max(1,bdam-a); if (h<=0) return 0;
  }
}
END {
  best=0;
  print "Boss: " bhit " "bdam" / "barm
  for (w in weapon)
  for (a in armor)
  for (r1 in ring)
  for (r2 in ring) {
    if (!win(hit,dam[w]+dam[r1]+dam[r2],arm[a]+arm[r1]+arm[r2])) {
      c = cost[w]+cost[a]+cost[r1]+cost[r2];
      if (c > best) {
        print "Me: " hit " " dam[w]+dam[r1]+dam[r2] " / " arm[a]+arm[r1]+arm[r2];
        verbose=1; win(hit,dam[w]+dam[r1]+dam[r2],arm[a]+arm[r1]+arm[r2]); verbose=0;
        print "Win: w="w" a="a" r1="r1" r2="r2" cost:"c;
        best=c;
      }
    }
  }
  print best;
}
