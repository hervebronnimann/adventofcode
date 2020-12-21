function add(x,n) { split(x,v,":"); sue[n,v[1]] = v[2]; }
function filter(x,n) { split(x,v,":");
  if ((n,v[1]) in sue) {
    if (v[1]=="cats" || v[1]=="trees") return sue[n,v[1]] > v[2];
    if (v[1]=="pomeranians" || v[1]=="goldfish") return sue[n,v[1]] < v[2];
    return sue[n,v[1]] == v[2];
  }
  return 1;
}
{ add($2,$1); add($3,$1); add($4,$1); }
END {
  for (n=1; n<=NR; ++n) {
    if (!filter("children:3", n)) continue;
    if (!filter("cats:7", n)) continue;
    if (!filter("samoyeds:2", n)) continue;
    if (!filter("pomeranians:3", n)) continue;
    if (!filter("akitas:0", n)) continue;
    if (!filter("vizslas:0", n)) continue;
    if (!filter("goldfish:5", n)) continue;
    if (!filter("trees:3", n)) continue;
    if (!filter("cars:2", n)) continue;
    if (!filter("perfumes:1", n)) continue;
    print "Aunt Sue " n;
  }
}
