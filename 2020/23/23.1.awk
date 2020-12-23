BEGIN { num_moves = 100; }
function prev(d) { return d==1?len:d-1; }
function cw(p) { return p==len?1:p+1; }
function find_dest(d,d1,d2,d3) { d = prev(d); while (d==d1||d==d2||d==d3) d = prev(d); return d; }
function init(s) {
  split(s,cups,"");
  current = cups[1]; len=length(s);
  for (i in cups) { next_cup[cups[i]] = cups[cw(i)]; }
}
$1 { init($1); } 
END {
  if (current == "") init("167248359");
  for (move=1; move<=num_moves; ++move) {
    print "-- move " move " --";
    d1=next_cup[current]; d2=next_cup[d1]; d3=next_cup[d2];
    dest = find_dest(current,d1,d2,d3);
    c="cups:"; cc = cups[1];
    for (i=1;i<=len;++i) { if (cc == current) c = c " (" cc ")"; else c = c " " cc; cc = next_cup[cc]; }
    print c;
    print "pick up: " d1 ", " d2 ", " d3;
    print "destination: " dest;
    print;
    next_cup[current] = next_cup[d3];
    dd = next_cup[dest];
    next_cup[d3] = dd;
    next_cup[d2] = d3;
    next_cup[d1] = d2;
    next_cup[dest] = d1;
    current = next_cup[current];
  }
  current = 1;
  for (i=next_cup[current]; i != current; i=next_cup[i]) res = res i;
  print res;
}
