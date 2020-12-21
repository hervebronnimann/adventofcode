{ 
  for (i=1; i <= NF; ++i) {
    if ($i == "contains") {
      k = 0;
      for (++i; i <= NF; ++i) {
        if (!($i in allergens)) { allergens[$i] = 1; ++n_allergens; print "Found allergen " $i; }
        ag[$i,++nag[$i]] = NR;
      }
    } else {
      if (!($i in foods)) { foods[$i] = 1; ++n_foods; print "Found food " $i; }
      food[NR,$i] = 1; ++foodn[NR];
    }
  }
}

function print_inter() {
  line = ""
  for (j=1; j<=n_inter; ++j) line = line " " inter[j];
  print line;
}

function intersection(nfood) {
  for (j=1; j<=n_inter; ) {
    if ((nfood,inter[j]) in food) ++j; else inter[j] = inter[n_inter--];
  }
}

END {
  # Identify all the allergens one by one
  n = n_allergens;
  while (n > 0)  {
    # Find an allergen that is the only one in the intersection of all its food ingredients
    found = 0;
    for (a in allergens) {
      # Invariant: name contains all the allergens determined so far, and fname contains their food names.
      if (name[a] != "") continue;
      print "Trying allergen " a;
      # Populate foods with all that haven't been named, then winnow each food that contains allergen
      n_inter = 0;
      for (f in foods)
        if (!(f in fname))
          { inter[++n_inter] = f; print "Trying with food " f; }
      # Trim the foods that are not in food[f,*] from inter array, for each f in set ag[a].
      for (i=1; i<=nag[a]; ++i) { intersection(ag[a,i]); print "Removing foods not in " ag[a,i] " remains " n_inter; print_inter() }
      # If only one food remains, then allergen is that food, we can iterate
      if (n_inter == 1) {
        print "Allergen " a " is " inter[1]
        name[a] = inter[1]; fname[inter[1]] = a; --n;
        found = 1; break;
      }
    }
    if (found == 0) {
      print "Couldn't find food, remains " n " allergens unknown";
      exit;
    }
  }
  # Count those who cannot be allergens;
  sum = 0;
  for (x in food) {
    split(x,xx,SUBSEP);
    if (!(xx[2] in fname)) ++sum;
  }
  print sum
}
