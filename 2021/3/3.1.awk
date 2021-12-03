{ 
  for (i=1; i<=NF; ++i) cnt[i,$i] = cnt[i,$i]+1; n = NF
  line[NR] = $0;
}
END  {
  p2=2**(n-1);
  for (i=1; i<=n; ++i) {
    if (cnt[i,1]>cnt[i,0]) epsilon += p2; else gamma += p2;
    p2 /= 2;
  }
  print epsilon * gamma;
}
