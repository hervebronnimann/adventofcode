BEGIN {
  split("97,61,53,101,131,163,79,103,67,127,71,109,89,107,83,73,113,59,137,139",ticket,",");
}
/^[a-z_]*:/ { 
  split($2,r,"-"); min1[NR] = r[1]; max1[NR] = r[2];
  split($4,r,"-"); min2[NR] = r[1]; max2[NR] = r[2];
  name[++n_field] = $1; next;
}
/^$/ {
  print "FIELDS " n_field; next;
}
{
  # Store everything into a matrix for further processing
  ++n_ticket; split($1,field,",");
  for (j in field) fields[n_ticket,j] = field[j];
}
END {
  for (j=1; j <= n_field; ++j) {
    candidates = "";
    for (k=1; k <= n_field; ++k) {
      # print "Trying mapping " name[k] " for field " j;
      found = 1;
      for (i=1; i <= n_ticket; ++i)
         if (!( (fields[i,j] >= min1[k] && fields[i,j] <= max1[k]) || (fields[i,j] >= min2[k] && fields[i,j] <= max2[k]) )) {
           # print "Exception row " i ": " fields[i,j] " not in " min1[k] "," max1[k] " nor " min2[k] "," max2[k];;
           found = 0; break;
         }
      candidates = candidates "\t" (found ? k : 0);
      if (found > 0) { num[j] += 1; c[j,k] = 1; }
    }
    print "Field " j " could be " num[j] "\t[ " candidates;
  }
  res = 1;
  for (n=1; n <= n_field; ++n)
    for (j=1; j <= n_field; ++j)
      if (num[j] == 1) {
	for (k=1; k <= n_field; ++k)
          if (((j,k) in c) && !(k in m)) {
            print "Field " j " is " name[k] " " k; m[k] = j;
	    if (name[k] ~ /^departure_/) res *= ticket[j];
	    break;
          }
	for (t=1; t <= n_field; ++t) { num[t] -= 1; }
        break;
      }
  print res;
}
