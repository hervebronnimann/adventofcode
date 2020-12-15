BEGIN {
  split("97,61,53,101,131,163,79,103,67,127,71,109,89,107,83,73,113,59,137,139",ticket,",");
}
/^[a-z_]*:/ { 
  k = 0; name[++n_field] = $1;
  for (i=2; i <= NF; ++i) {
    if ($i == "or") continue;
    ++k; split($i,r,"-");
    min[NR,k] = r[1]; max[NR,k] = r[2];
    # print name[NR] " has range " k, r[1] "," r[2]
  }
  next;
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
      for (i=1; i <= n_ticket; ++i) {
         valid = 0;
	 for (t=1; (k,t) in min; ++t)
           if (fields[i,j] >= min[k,t] && fields[i,j] <= max[k,t]) { valid = 1; break; }
         if (valid == 0) {
           # print "Exception row " i ": " fields[i,j] " not in " min[k,1] "," max[k,1] " nor " min[k,2] "," max[k,2];;
           found = 0; break;
         }
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
