BEGIN { d[-1]=1; d[0]=1; d[1]=1; }
{
  split($1,c,""); cols = length($1); rows = NR;
  for (j=1; j<=cols; ++j) lights[rows,j] = c[j]=="#"?1:0;
}
END {
  for (n=1; n<=100; ++n) {
    for (i=1; i<=rows; ++i)
    for (j=1; j<=cols; ++j) {
      count = 0; for (ii in d) for (jj in d) if ((ii!=0 || jj!=0) && lights[i+ii,j+jj]) ++count;
      if (lights[i,j]) lights2[i,j] = (count==2 || count==3); else lights2[i,j] = count==3;
    }
    for (i=1; i<=rows; ++i)
    for (j=1; j<=cols; ++j) {
      lights[i,j] = lights2[i,j];
    }
    lights[1,1] = 1;
    lights[1,cols] = 1;
    lights[rows,1] = 1;
    lights[rows,cols] = 1;
  }
  count = 0;
  for (i=1; i<=rows; ++i)
  for (j=1; j<=cols; ++j) {
    count += lights[i,j];
  }
  print count;
}
