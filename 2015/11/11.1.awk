BEGIN { split("abcdefghijklmnopqrstuvwxyz",c,""); for (i=1;i<=26;++i) { map[c[i]]=i; unmap[i]=c[i]; } }
function psplit(x) { split(x,pa,""); plen=length(x); for (i in pa) p[i] = map[pa[i]]; delete pa; }
function pjoin() { s=""; for (i=1; i<=plen; ++i) s = s unmap[p[i]]; return s; }
function nextp() { i=plen; while (++p[i]==27) { p[i]=1; --i; }; }
function valid() {
  for (i in p)
    if (p[i]==map["i"] || p[i]==map["l"] || p[i]==map["o"]) return 0;
  found3=0; haspair=(p[1]==p[2]); pair=p[2]; found=0;
  for (i=3;i<=plen;++i) {
    if (p[i-1]==p[i-2]+1 && p[i]==p[i-1]+1) found3=1;
    if (p[i-1]==p[i]) {
      if (!haspair) { haspair=1; pair=p[i]; }
      else if (p[i]!=pair) { found=1; }
    }
  }
  return found3 && found;
}
{
  psplit($1); 
  do { nextp(); if (verbose) print(pjoin()); } while (!valid());
  print(pjoin());
}
