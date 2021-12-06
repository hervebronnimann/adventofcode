function min(x,y) { return x<y ? x : y }
function max(x,y) { return x>y ? x : y }
function sumgt1(b) { _sum=0; for (_x in b) if (b[_x]>1) ++_sum; return _sum } 
$1 == $4 { for (i=min($2,$5); i<=max($2,$5); ++i) ++b[$1,i] }
$2 == $5 { for (i=min($1,$4); i<=max($1,$4); ++i) ++b[i,$2] }
END { print sumgt1(b) }
