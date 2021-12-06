function sum(b) { _sum=0; for (_x in b) _sum+=b[_x]; return _sum } 
{ split($1,fish,","); n=length(fish); print length(fish) }
END {
  for (x in fish) ++nfish[fish[x]];
  for (d=1;d<=256;++d) {
    n0 = nfish[0];
    for (i=1;i<=8;++i) nfish[i-1]=nfish[i];
    nfish[6]+=n0;
    nfish[8]=n0;
  }
  print sum(nfish);
}
