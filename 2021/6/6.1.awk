{ split($1,fish,","); n=length(fish); print length(fish) }
END {
  for (d=1;d<=80;++d) {
    for (x in fish) { if (fish[x]>0) f2[x]=fish[x]-1; else { f2[x]=6; f2[++n]=8 } }
    delete fish
    for (x in f2) fish[x]=f2[x]
  }
  print length(fish);
}
