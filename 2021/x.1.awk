# General utilities
function abs(x) { return x<0 ? -x:x }
function min(x,y) { return x<y ? x : y }
function max(x,y) { return x>y ? x : y }
# Working with arrays
function array_swap(a,i,j) { _t = a[i]; a[i] = a[j]; a[j] = _t }
function array_sort(a) {
  do {
    _haschanged = 0
    for(_i=1; _i < length(a); _i++)
      if (a[_i] > a[_i+1]) {
        array_swap(a,_i,_i+1); _haschanged = 1
      }
  } while (_haschanged == 1)
}
function reverse(a) { _i=length(a); for (_j=1;_j<_i;++_j) { array_swap(a,_i,_j); --_i } }
# Working with associative maps
function sample(x) { for (_i in x) return _i; }
function minpos(x) { _imin=sample(x); for (_i in x) if (x[_i]<x[_imin]) _imin=_i; return _imin }
function maxpos(x) { _imax=sample(x); for (_i in x) if (x[_i]>x[_imax]) _imax=_i; return _imax }
function sum(b) { _sum=0; for (_x in b) _sum+=b[_x]; return _sum } 
# Working with strings
function string_join(a) { _str=""; for(_j=1;_j<=length(a);++_j) _str=_str a[_j]; return _str }
function string_sort(str) { split(str,_a,""); array_sort(_a); return string_join(_a) }
function string_reverse(str) { split(str,_a,""); reverse(_a); return string_join(_a) }
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
