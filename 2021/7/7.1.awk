function abs(x) { return x<0 ? -x : x }
function min(x,y) { return x<y ? x : y }
function max(x,y) { return x>y ? x : y }
function minpos(x) { _imin=1; for (_i in x) if (x[_i]<x[_imin]) _imin=_i; return _imin }
function maxpos(x) { _imax=1; for (_i in x) if (x[_i]>x[_imax]) _imax=_i; return _imax }
{ split($1,pos,","); x0=pos[minpos(pos)]; x1=pos[maxpos(pos)]; }
END {
  M=0; for (i in pos) M += abs(pos[i])
  for (x=x0; x<=x1; ++x) {
    m=0; for (i in pos) m += abs(pos[i]-x)
    if (m < M) { M=m; mx=x }
  }
  print mx, M;
}
