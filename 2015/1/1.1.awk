{ split($0,c,"");
  for (i=1;i<=length($0);++i) { if (c[i]=="(") ++l; else --l; }
  print l;
}
