BEGIN {
  if (init=="") init = "167248359"; if (num_moves==0) num_moves = 100;
  split(init,cups,""); pos=1; len=length(init); }
function prev(label) { return label==1?len:label-1; }
function cw(p) { return p==len?1:p+1; }
function find_dest(d,d1,d2,d3) { d = prev(d); while (d==d1||d==d2||d==d3) d = prev(d); return d; }
function find(label) { for (i=1; i<=len; ++i) if (cups[i]==label) return i; return 0; }
function remove_pos(p) { for (i=p; cups[i+1] != ""; ++i) cups[i] = cups[i+1]; cups[i]=""; --len; }
function remove(d) { remove_pos(find(d)); }
END {
  for (move=1; move<=num_moves; ++move) {
    print "-- move " move " --";
    current = cups[pos];
    p1=cw(pos); p2=cw(p1); p3=cw(p2);
    d1=cups[p1]; d2=cups[p2]; d3=cups[p3];
    dest = find_dest(current,d1,d2,d3);
    c="cups:";
    for (i=1;i<=len;++i) if (i==pos) c = c " (" cups[i] ")"; else c = c " " cups[i];
    print c;
    print "pick up: " d1 ", " d2 ", " d3;
    print "destination: " dest
    print;
    remove(d3); remove(d2); remove(d1);
    pdest = find(dest);
    for (i=len+3; i>pdest+3; --i) cups[i] = cups[i-3];
    cups[i--] = d3; cups[i--] = d2; cups[i--] = d1; cups[i] = dest; len += 3;
    pos = cw(find(current));
  }
  pos = find(1);
  for (i=cw(pos); i!=pos; i=cw(i)) res = res cups[i];
  print res;
}
