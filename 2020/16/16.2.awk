/^[a-z_]*:/ { 
  split($2,r,"-"); min1[NR] = r[1]; max1[NR] = r[2];
  split($4,r,"-"); min2[NR] = r[1]; max2[NR] = r[2];
  print $0; next;
}
/^$/ {
  print; next;
}
{
  split($1,field,",");
  all_valid = 1;
  for (n in field) {
    valid = 0;
    for (j in field)
      if ((field[n] >= min1[j] && field[n] <= max1[j]) || (field[n] >= min2[j] && field[n] <= max2[j])) {
        valid=1; break;
      }
    if (valid == 0) { all_valid = 0; break;}
  }
  if (all_valid == 1) print $0;
}
