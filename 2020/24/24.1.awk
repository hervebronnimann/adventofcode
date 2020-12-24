{ split($1,d,"");
  x = 0; y = 0; dx = 2;
  for (i=1; i <= length($1); ++i) {
    if (d[i] == "s") { y-=1; dx = 1; }
    else if (d[i] == "n") { y+=1; dx = 1; }
    else if (d[i] == "e") { x += dx; dx = 2; }
    else if (d[i] == "w") { x -= dx; dx = 2; }
    else print "WTF unknown letter " $1 " " i;
  }
  if (dx == 1) print "WTF ending in s or n" $1;
  tile[x,y] = 1 - tile[x,y];
}
END {
  res = 0;
  for (ij in tile) {
    split(ij,sep,SUBSEP);
    if (tile[sep[1],sep[2]] == 1) ++res;
  }
  print res;
}
