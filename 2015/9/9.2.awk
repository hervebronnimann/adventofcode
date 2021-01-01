function max(x,y) { return x>y ? x : y; }
function push(x) { q[++qk] = x; }
function pop() { return q[qk--]; }
function mts(k) {
  loc[k] = 0;  # mark occupied
  res2 = 0;
  for (j in loc) if (loc[j] == 1) { push(res2); push(j); delta = mts(j); j = pop(); res2 = pop(); res2 = max(res2, dist[k,j] + delta); }
  loc[k] = 1; 
  return res2;
}
BEGIN { qk = 0; }
{ loc[$1] = 1; loc[$3] = 1; dist[$1,$3] = $5; dist[$3,$1] = $5; }
END {
  res = 0;
  for (i in loc) res = max(res, mts(i));
  print res;
}
