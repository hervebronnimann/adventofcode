function min(x,y) { return x<y? x : y; }
function max(x,y) { return x>y? x : y; }
function set(x1,x2,y1,y2,v) { for (x=x1; x<=x2; ++x) for (y=y1; y<=y2; ++y) lights[x,y] = v; }
function tog(x1,x2,y1,y2)   { for (x=x1; x<=x2; ++x) for (y=y1; y<=y2; ++y) lights[x,y] = 1-lights[x,y]; }
function cnt(x1,x2,y1,y2)   { res = 0; for (x=x1; x<=x2; ++x) for (y=y1; y<=y2; ++y) res += lights[x,y]; return res; }
BEGIN { set(0,999,0,999,0); print cnt(0,999,0,999); }
/^on/     { set(min($2,$5),max($2,$5),min($3,$6),max($3,$6),1); }
/^off/    { set(min($2,$5),max($2,$5),min($3,$6),max($3,$6),0); }
/^toggle/ { tog(min($2,$5),max($2,$5),min($3,$6),max($3,$6)); }
END { print cnt(0,999,0,999); }
