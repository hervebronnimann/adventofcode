BEGIN { if (target==0) target=150; }
{ jug[NR] = $1 }
END {
  # num[j,i] ways of meeting target j with a subset of jugs 1..i
  num[0,0] = 1;
  for (i=1;i<=NR;++i)
    for (j=0; j<=target; ++j)
      num[j,i] = num[j,i-1] + num[j-jug[i],i-1]
  print target " " num[target,NR]
}
