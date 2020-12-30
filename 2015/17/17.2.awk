BEGIN { if (target==0) target=150; }
{ jug[NR] = $1 }
END {
  # num[k,j,i] ways of meeting target j with exactly k jugs from jugs 1..i
  num[0,0,0] = 1;
  for (k=0;k<=NR;++k) {
    for (i=1;i<=NR;++i)
      for (j=0; j<=target; ++j)
        num[k,j,i] = num[k,j,i-1] + num[k-1,j-jug[i],i-1]
    if (num[k,target,NR]>0) { print target " " k " " num[k,target,NR]; break; }
  }
}
