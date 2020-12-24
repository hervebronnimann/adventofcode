function black(i,j) { return (i,j) in tile && tile[i,j] == 1 ? 1 : 0; }
function flip_tile(i,j) { if ((i,j) in tile) tile[i,j] = 1-tile[i,j]; else tile[i,j] = 1; }
/[ensw]+/ {
  split($1,d,""); x = 0; y = 0; dx = 2;
  for (i=1; i <= length($1); ++i) {
    if (d[i] == "s") { y-=1; dx = 1; }
    else if (d[i] == "n") { y+=1; dx = 1; }
    else if (d[i] == "e") { x += dx; dx = 2; }
    else if (d[i] == "w") { x -= dx; dx = 2; }
    else print "WTF unknown letter " $1 " " i;
  }
  if (dx == 1) print "WTF ending in 's' or 'n'" $1;
  flip_tile(x,y);
  if (verbose) print "Directions " NR " tile:" x ", " y
}
END {
  res = 0; for (ij in tile) { split(ij,sep,SUBSEP); if (tile[sep[1],sep[2]]) ++res; }
  print res;
}
