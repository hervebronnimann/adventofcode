function clone(lhs, rhs) {
  for (i = 1; i <= maxNR; ++i)
  for (j = 1; j <= maxNF; ++j) {
    lhs[i,j] = rhs[i,j];
  }
}
function neighbors2(i, j) {
  n = 0;
  if (board2[i-1,j-1] == "#") ++n;
  if (board2[i-1,j]   == "#") ++n;
  if (board2[i-1,j+1] == "#") ++n;
  if (board2[i,j-1]   == "#") ++n;
  if (board2[i,j+1]   == "#") ++n;
  if (board2[i+1,j-1] == "#") ++n;
  if (board2[i+1,j]   == "#") ++n;
  if (board2[i+1,j+1] == "#") ++n;
  return n;
}
/^[.#L]*$/ {
  split($1, row, "");
  for (j in row) board[NR,j] = row[j];
  maxNR = NR; maxNF = length(row);
  print maxNR, maxNF;
}
END {
  for (iter = 1; iter > 0; ) {
    iter = 0;
    clone(board2, board);
    for (i = 1; i <= maxNR; ++i)
    for (j = 1; j <= maxNF; ++j) {
      if (board2[i, j] == ".") continue;
      x = neighbors2(i, j);
      if (board2[i, j] == "L" && x == 0) { board[i, j] = "#"; ++iter; }
      if (board2[i, j] == "#" && x >= 4) { board[i, j] = "L"; ++iter; }
    }
    print "** Iter: " iter;
  }
  n = 0;
  for (i = 1; i <= maxNR; ++i)
  for (j = 1; j <= maxNF; ++j) {
    if (board[i,j] == "#") ++n;
  }
  print n;
}
