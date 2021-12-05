function min(x,y) { if (x<y) return x; return y; }
function max(x,y) { if (x>y) return x; return y; }
$1 == $4 { for (i=min($2,$5); i<=max($2,$5); ++i) ++b[$1,i]; }
$2 == $5 { for (i=min($1,$4); i<=max($1,$4); ++i) ++b[i,$2]; }
END { for (p in b) { if (b[p]>1) ++n; } print n; }
