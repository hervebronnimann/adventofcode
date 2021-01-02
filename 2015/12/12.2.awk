function isnum(y) { return y=="0" || y=="1" || y=="2" || y=="3" || y=="4" || y=="5" || y=="6" || y=="7" || y=="8" || y=="9" || y=="-"; }
function push(x) { p[++pq] = x; }
function top() { return p[pq]; }
function pop() { return p[pq--]; }
function removered() {
  for (i=1; i<=len; ++i) {
    if (c[i]=="{") { push(i); continue;}
    if (c[i]=="}") { pop(); continue;}
    if (i+5<=len && c[i]==":" && c[i+1]=="\"" && c[i+2]=="r" && c[i+3]=="e" && c[i+4]=="d" && c[i+5]=="\"") {
      for (level=1; i<=len && level>0; ++i) {
        if (c[i]=="{") ++level; else if (c[i]=="}") --level;
      }
      for (j=top()+1; j<i; ++j) c[j] = ""; # white out all the object containing red;
      pop();
    }
  }
}
{
  split($1,c,""); len=length($1);
  removered();
  i=1; res = 0;
  while (i<=len) {
    while (i<=len && !isnum(c[i])) ++i; 
    neg=1; if (i<=len && c[i]=="-") { neg=-1; ++i; }
    x=0; while (i<=len && isnum(c[i])) { x = x*10+c[i]; ++i; }
    if (verbose) print neg*x;
    res += neg*x;
  }
  print res;
}
