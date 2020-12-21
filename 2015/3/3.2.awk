{ split($0,c,"");
  sx=0; sy=0; ++house[sx,sy]
  rx=0; ry=0; ++house[rx,ry]
  for (i=1;i<=length($0);++i) {
    if (i%2==1) {
      if (c[i]=="^") ++sy; else
      if (c[i]=="v") --sy; else
      if (c[i]==">") ++sx; else
      if (c[i]=="<") --sx; else { print "WTF"; exit; }
      ++house[sx,sy];
    } else {
      if (c[i]=="^") ++ry; else
      if (c[i]=="v") --ry; else
      if (c[i]==">") ++rx; else
      if (c[i]=="<") --rx; else { print "WTF"; exit; }
      ++house[rx,ry];
    }
  }
  for (xy in house) ++n;
  print n;
}
