/=>/ { from[NR]=$1; to[NR]=$3; next; }
/^$/ { next; }
{
  for (i in from) {
    j = 1; s = gensub(from[i],to[i],j,$0); while (s != $0) { rep[s] = 1; ++j; s = gensub(from[i],to[i],j,$0); }
  }
  count = 0; for (i in rep) ++count; print count;
}
