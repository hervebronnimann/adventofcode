function min(x,y) { return x<y?x:y; }
function max(x,y) { return x>y?x:y; }
function dist(t,d) {
  runs = int(t / (run[d] + rest[d]));
  rem = t - runs * (run[d] + rest[d]);
  return speed[d] * (run[d] * runs + min(rem,run[d]));
}
BEGIN { race = 2503; } 
{ deers[$1] = 1; speed[$1] = $4; run [$1]= $7; rest [$1]= $14; }
END {
  for (t=1; t<=race; ++t) {
    maxdt = 0;
    for (d in deers) { dt[d] = dist(t,d); maxdt=max(maxdt,dt[d]); }
    for (d in deers) if (dt[d]==maxdt) ++points[d];
  }
  maxp = 0;
  for (d in speed) maxp=max(points[d],maxp);
  print maxp;
}
