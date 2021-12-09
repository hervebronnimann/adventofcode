{ split($0,a,""); n=length(a); for (i=1;i<=n;++i) b[NR,i]=a[i]; m=NR }
END {
  print n, m
  for (i=1;i<=m;++i) { b[i,0]=99; b[i,n+1]=99 }
  for (j=1;j<=n;++j) { b[0,j]=99; b[m+1,j]=99 }
  for (i=1;i<=m;++i)
  for (j=1;j<=n;++j) {
    if (b[i,j]<b[i+1,j] && b[i,j]<b[i-1,j] && b[i,j]<b[i,j+1] && b[i,j]<b[i,j-1]) {
      # print b[i,j] " at " i " " j
      risk+=b[i,j]+1;
    }
  }
  print risk;
}
