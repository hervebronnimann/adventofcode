function abs(x) { return x<0 ? -x : x }
function sample(x) { for (_i in x) return _i; }
function minpos(x) { _imin=sample(x); for (_i in x) if (x[_i]<x[_imin]) _imin=_i; return _imin }
function maxpos(x) { _imax=sample(x); for (_i in x) if (x[_i]>x[_imax]) _imax=_i; return _imax }
function f(x) { return x*(x+1)/2; }
function cost(x,pos) { _m=0; for (_i in pos) _m += f(abs(pos[_i]-x)); return _m }
{ split($1,pos,","); x0=pos[minpos(pos)]; x3=pos[maxpos(pos)]; }
END {
  M0=cost(x0,pos);
  M3=cost(x3,pos);
  while (x0+5 < x3) {
    x1 = int(x0 + (x3-x0)/3); M1 = cost(x1,pos);
    x2 = int(x3 - (x3-x0)/3); M2 = cost(x2,pos);
    # print x0, x1, x2, x3, M0, M1, M2, M3
    if (M1<=M2) { x3=x2; M3=M2 }
    if (M2<=M1) { x0=x1; M0=M1 }
  }
  for (x=x0;x<=x3;++x) { c[x] = cost(x,pos); print x, c[x]; }
  x=minpos(c);
  print x, c[x]
}
