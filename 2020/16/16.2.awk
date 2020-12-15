/^[a-z_]*:/ { 
  k = 0;
  print $0;
  for (i=2; i <= NF; ++i) {
    if ($i == "or") continue;
    ++k; split($i,r,"-");
    min[NR,k] = r[1]; max[NR,k] = r[2];
    # print name[NR] " has range " k, r[1] "," r[2]
  }
  next;
}
/^$/ {
  print; next;
}
{
  split($1,field,",");
  all_valid = 1;
  for (n in field) {
    valid = 0;
    for (j in field) {
      for (t=1; (j,t) in min; ++t)
        if (field[n] >= min[j,t] && field[n] <= max[j,t]) { valid=1; break; }
      if (valid == 1) break;
    }
    if (valid == 0) { all_valid = 0; break;}
  }
  if (all_valid == 1) print $0;
}
