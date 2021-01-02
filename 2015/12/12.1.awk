function isnum(y) { return y=="0" || y=="1" || y=="2" || y=="3" || y=="4" || y=="5" || y=="6" || y=="7" || y=="8" || y=="9" || y=="-"; }
{
  split($1,c,""); len=length($1); i=1;
  res = 0;
  while (i<=len) {
    while (i<=len && !isnum(c[i])) ++i; 
    neg=1; if (i<=len && c[i]=="-") { neg=-1; ++i; }
    x=0; while (i<=len && isnum(c[i])) { x = x*10+c[i]; ++i; }
    if (verbose) print neg*x;
    res += neg*x;
  }
  print res;
}
