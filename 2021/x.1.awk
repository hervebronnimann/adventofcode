# General utilities
function min(x,y) { return x<y ? x : y }
function max(x,y) { return x>y ? x : y }
function sum(b) { _sum=0; for (_x in b) _sum+=b[_x]; return _sum } 
# Working with strings
function reverse(str) { _str=""; for(_j=length(str);_j>0;--_j) _str=_str substr(str,_j,1); return _str }
# Working with rectangular grids
function read_board(b,nr,row) {
  split(row, _row, "");
  for (_j in _row) b[nr,j_] = _row[_j];
  maxNR = NR; maxNF = length(_row);
}
function clone_board(lhs, rhs) {
  for (_i = 1; _i <= maxNR; ++_i)
  for (_j = 1; _j <= maxNF; ++_j) {
    lhs[_i,_j] = rhs[_i,_j];
  }
}
function count_neighbors(b,ix,i,j) {
  _n = 0;
  for if (b[i-1,j-1] == x) ++_n;
  if (b[i-1,j]   == x) ++_n;
  if (b[i-1,j+1] == x) ++_n;
  if (b[i,j-1]   == x) ++_n;
  if (b[i,j+1]   == x) ++_n;
  if (b[i+1,j-1] == x) ++_n;
  if (b[i+1,j]   == x) ++_n;
  if (b[i+1,j+1] == x) ++_n;
  return _n;
}
