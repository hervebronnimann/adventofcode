function max(x,y) { return x>y ? x : y; }
function push(x) { q[++qk] = x; }
function pop() { return q[qk--]; }
function mts(k) {
  loc[k] = 0;  # mark seated
  res2 = -999999999;
  for (j in loc) if (loc[j] == 1) { push(res2); push(j); delta = mts(j); j = pop(); res2 = pop(); res2 = max(res2, dist[k,j] + dist[j,k] + delta); }
  loc[k] = 1; 
  return res2 == -999999999 ? dist[k,seed] + dist[seed,k] : res2;
}
{
  if (seed=="") seed = $1;  # Alice
  neg=1; if ($3=="lose") neg=-1;
  loc[$1] = 1; loc[$11] = 1;
  dist[$1,$11] += neg*$4;
}
END { print mts(seed); }
