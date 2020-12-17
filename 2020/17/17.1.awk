function enlarge() {
  --minX; --minY; --minZ;
  ++maxX; ++maxY; ++maxZ;
  for (i = minX; i <= maxX; ++i)
  for (j = minY; j <= maxY; ++j) 
  for (k = minZ; k <= maxZ; ++k) {
    if ((i == minX || i == maxX) || (j == minY || j == maxY) || (k == minZ || k == maxZ))
      board[i,j,k] = ".";
  }
}
function clone(lhs, rhs) {
  for (i = minX; i <= maxX; ++i)
  for (j = minY; j <= maxY; ++j) 
  for (k = minZ; k <= maxZ; ++k) {
    lhs[i,j,k] = rhs[i,j,k];
  }
}
function neighbors3(i, j, k) {
  n = 0;
  for (dx in neighbors)
  for (dy in neighbors)
  for (dz in neighbors) {
    if (dx == 0 && dy == 0 && dz == 0) continue;
    if (!((i+dx,j+dy,k+dz) in board2)) continue;
    if (board2[i+dx,j+dy,k+dz] == "#") ++n;
  }
  return n;
}
BEGIN {
  neighbors[-1] = 1; neighbors[0] = 1; neighbors[1] = 1;
  minX = 1; minY = 1; minZ = 0;
}
/^[.#]*$/ {
  split($1, row, "");
  for (j in row) board[NR,j,0] = row[j];
  maxX = NR; maxY = length(row); maxZ = 0;
  print minX ".." maxX " x " minY ".." maxY " x " minZ ".." maxZ;
}
END {
  for (iter = 1; iter <= 6; ++iter) {
    active = 0; changed = 0;
    enlarge();
    clone(board2, board);
    for (i = minX; i <= maxX; ++i)
    for (j = minY; j <= maxY; ++j) 
    for (k = minZ; k <= maxZ; ++k) {
      x = neighbors3(i, j, k);
      if (board2[i,j,k] == "." && x == 3) {board[i,j,k] = "#"; ++changed;}
      if (board2[i,j,k] == "#" && (x <2 || x > 3)) {board[i,j,k] = "."; ++changed;}
      if (board2[i,j,k] == "#") ++active;
    }
    delete board2;
    print "Iter " iter ": " minX ".." maxX " x " minY ".." maxY " x " minZ ".." maxZ " active:" active " changed:" changed;
  }
  for (i = minX; i <= maxX; ++i)
  for (j = minY; j <= maxY; ++j) 
  for (k = minZ; k <= maxZ; ++k) {
      if (board[i,j,k] == "#") ++sum;
  }
  print sum;
}
