function min(x,y) { return x<y? x : y; }
function max(x,y) { return x>y? x : y; }
function dec(x1,x2,y1,y2,v) { for (x=x1; x<=x2; ++x) for (y=y1; y<=y2; ++y) lights[x,y] = max(0,lights[x,y]-v); }
function inc(x1,x2,y1,y2,v) { for (x=x1; x<=x2; ++x) for (y=y1; y<=y2; ++y) lights[x,y] += v; }
function cnt(x1,x2,y1,y2)   { res = 0; for (x=x1; x<=x2; ++x) for (y=y1; y<=y2; ++y) res += lights[x,y]; return res; }
BEGIN { inc(0,999,0,999,0); print cnt(0,999,0,999); }
/^on/     { inc(min($2,$5),max($2,$5),min($3,$6),max($3,$6),1); }
/^off/    { dec(min($2,$5),max($2,$5),min($3,$6),max($3,$6),1); }
/^toggle/ { inc(min($2,$5),max($2,$5),min($3,$6),max($3,$6),2); }
END { print cnt(0,999,0,999); }
