function enlarge() {
  --minX; --minY; --minZ; --minW;
  ++maxX; ++maxY; ++maxZ; ++maxW;
  for (i = minX; i <= maxX; ++i)
  for (j = minY; j <= maxY; ++j) 
  for (k = minZ; k <= maxZ; ++k)
  for (m = minW; m <= maxW; ++m) {
    if ((i == minX || i == maxX) || (j == minY || j == maxY) || (k == minZ || k == maxZ) || (m == minW || m == maxW))
      board[i,j,k,m] = ".";
  }
}
function clone(lhs, rhs) {
  for (i = minX; i <= maxX; ++i)
  for (j = minY; j <= maxY; ++j) 
  for (k = minZ; k <= maxZ; ++k)
  for (m = minW; m <= maxW; ++m) {
    lhs[i,j,k,m] = rhs[i,j,k,m];
  }
}
function neighbors4(i, j, k, m) {
  n = 0;
  for (dx in neighbors)
  for (dy in neighbors)
  for (dz in neighbors)
  for (dw in neighbors) {
    if (dx == 0 && dy == 0 && dz == 0 && dw == 0) continue;
    if (!((i+dx,j+dy,k+dz,m+dw) in board2)) continue;
    if (board2[i+dx,j+dy,k+dz,m+dw] == "#") ++n;
  }
  return n;
}
BEGIN {
  neighbors[-1] = 1; neighbors[0] = 1; neighbors[1] = 1;
  minX = 1; minY = 1; minZ = 0; minW = 0;
}
/^[.#]*$/ {
  split($1, row, "");
  for (j in row) board[NR,j,0,0] = row[j];
  maxX = NR; maxY = length(row); maxZ = 0; maxW = 0;
  print minX ".." maxX " x " minY ".." maxY " x " minZ ".." maxZ " x " minW ".." maxW;
}
END {
  for (iter = 1; iter <= 6; ++iter) {
    active = 0; changed = 0;
    enlarge();
    clone(board2, board);
    for (i = minX; i <= maxX; ++i)
    for (j = minY; j <= maxY; ++j) 
    for (k = minZ; k <= maxZ; ++k)
    for (m = minW; m <= maxW; ++m) {
      N = neighbors4(i, j, k, m);
      if (board2[i,j,k,m] == "." && N == 3) {board[i,j,k,m] = "#"; ++changed;}
      if (board2[i,j,k,m] == "#" && (N <2 || N > 3)) {board[i,j,k,m] = "."; ++changed;}
      if (board2[i,j,k,m] == "#") ++active;
    }
    delete board2;
    print "Iter " iter ": " minX ".." maxX " x " minY ".." maxY " x " minZ ".." maxZ " x " minW ".." maxW " active:" active " changed:" changed;
  }
  sum = 0;
  for (i = minX; i <= maxX; ++i)
  for (j = minY; j <= maxY; ++j) 
  for (k = minZ; k <= maxZ; ++k)
  for (m = minW; m <= maxW; ++m) {
      if (board[i,j,k,m] == "#") ++sum;
  }
  print sum;
}
