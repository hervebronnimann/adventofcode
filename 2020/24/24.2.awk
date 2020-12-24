function black(i,j) { return (i,j) in tile && tile[i,j] == 1 ? 1 : 0; }
function count_black() { res = 0; for (ij in tile) { split(ij,sep,SUBSEP); if (tile[sep[1],sep[2]]) ++res; }  return res; }
function flip_tile(i,j) { if ((i,j) in tile) tile[i,j] = 1-tile[i,j]; else tile[i,j] = 1; }
function queue_white(i,j) { if (!((i,j) in tile)) white[i,j] = 0; }
/[ensw]+/ { split($1,d,"");
  x = 0; y = 0; dx = 2;
  for (i=1; i <= length($1); ++i) {
    if (d[i] == "s") { y-=1; dx = 1; }
    else if (d[i] == "n") { y+=1; dx = 1; }
    else if (d[i] == "e") { x += dx; dx = 2; }
    else if (d[i] == "w") { x -= dx; dx = 2; }
    else print "WTF unknown letter " $1 " " i;
  }
  if (dx == 1) print "WTF ending in s or n" $1;
  flip_tile(x,y);
}
END {
  print "Day 0: " count_black();
  for (day=1; day <= 100 ; ++day) {
    # enqueue all neighbors of black not already in tile (they're white) into white array
    for (ij in tile) {
      split(ij,sep,SUBSEP); i = sep[1]; j = sep[2];
      if (tile[i,j] == 1) {
        queue_white(i-1,j-1); queue_white(i+1,j-1); queue_white(i-2,j); queue_white(i+2,j); queue_white(i-1,j+1); queue_white(i+1,j+1);
      }
    }
    # force color of check array as white
    for (ij in white) { split(ij,sep,SUBSEP); tile[sep[1],sep[2]] = 0; }
    delete white;
    # check all neighbors of existing tiles, enqueue all flips
    for (ij in tile) {
      split(ij,sep,SUBSEP); i = sep[1]; j = sep[2];
      n = black(i-1,j-1) + black(i+1,j-1) + black(i-2,j) + black(i+2,j) + black(i-1,j+1) + black(i+1,j+1)
      if (tile[i,j] == 1 && (n == 0 || n>2)) flip[i,j] = 0;
      if (tile[i,j] == 0 && n == 2) flip[i,j] = 1;
    }
    # perform the flips all at once
    for (ij in flip) { split(ij,sep,SUBSEP); flip_tile(sep[1],sep[2]); }
    delete flip;
    # count for the day
    if (day <= 10 || day%10 == 0) print "Day " day ": " count_black();
  }
}
