function max(x,y) { return x>y?x:y; }
BEGIN { if (tspoons=="") tspoons = 100; }
{ ++n; ingredient[$1] = 1; cap[$1]=$3; dur[$1]=$5; fla[$1]=$7; tex[$1]=$9; cal[$1]=$11; 
   print $1 " " cap[$1] " " dur[$1] " " fla[$1] " " tex[$1] " " cal[$1];
}
END {
  hscore = 0;
  for (i1=0; i1<=tspoons; ++i1) 
  for (i2=0; i1+i2<=tspoons; ++i2) 
  for (i3=0; i1+i2+i3<=tspoons; ++i3) {
    i4 = tspoons-i1-i2-i3;
    ccap=0; ddur=0; ffla=0; ttex=0; j=0;
    for (i in ingredient) {
       ++j; ts[i] = j==1?i1:j==2?i2:j==3?i3:i4;
       ccap += cap[i] * ts[i]; ddur += dur[i] * ts[i]; ffla += fla[i] * ts[i]; ttex += tex[i] * ts[i];
    }
    score = max(ccap,0) * max(ddur,0) * max(ffla,0) * max(ttex,0);
    # s = score " cap:" ccap " dur:" ddur " fla:" ffla " tex:" ttex " with"; for (i in ingredient) { s = s " " i ts[i]; } print s;
    if (score>hscore) hscore = score;
  }
  print hscore;
}
