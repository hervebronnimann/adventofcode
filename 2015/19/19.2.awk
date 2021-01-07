/=>/ { from[NR]=$1; to[NR]=$3; next; }
/^$/ { next; }
{ target=$1; }
function gen(x) {
  for (i in from) {
    j = 1; s = gensub(from[i],to[i],j,x); while (s != x) { rep2[s] = 1; ++j; s = gensub(from[i],to[i],j,x); }
  }
}
END {
  rep["e"] = 1; n = 0;
  while (!(target in rep)) {
    ++n;
    for (x in rep) gen(x); delete rep;
    for (x in rep2) rep[x] = 1; delete rep2;
  }
  print n;
}
