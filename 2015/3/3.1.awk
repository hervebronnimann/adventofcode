{ split($0,c,""); x=0; y=0; house[x,y] = 1;
  for (i=1;i<=length($0);++i) {
    if (c[i]=="^") ++y; else
    if (c[i]=="v") --y; else
    if (c[i]==">") ++x; else
    if (c[i]=="<") --x; else { print "WTF"; exit; }
    ++house[x,y];
  }
  for (xy in house) ++n;
  print n;
}
