/^[a-z_]*:/ { 
  ++k; split($2,r,"-"); min[k] = r[1]; max[k] = r[2];
  ++k; split($4,r,"-"); min[k] = r[1]; max[k] = r[2];
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
