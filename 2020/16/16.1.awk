/^[a-z_]*:/ { 
  for (i=2; i <= NR; ++i) {
    if ($i == "or") continue;
    split($i,r,"-");
    min[k] = r[1]; max[k] = r[2]; ++k;
  }
  next;
}
/^$/ {
  next;
}
{
  split($1,field,",");
  for (n in field) {
    valid = 0;
    for (k in min)
      if (field[n] >= min[k] && field[n] <= max[k]) { valid=1; break; }
    if (valid == 0) sum += field[n];
  }
}
END { print sum; }
