# A rule is either "[ab]" or "subrule [| subrule]*" with subrule a sequence of integer. Thus complex rules are : j1_k1 j1_k2 ... | j2_k1 j2_k2 ... 
# All match functions match a prefix of tok[l..r], return next l in range [l..r+1] to be checked if prefix match, 0 otherwise.
# If return l==r+1, then all the characters match exactly, with no other characters left to check.

function pushk(j) { stackk[++nk] = k; }
function popk() { return stackk[nk--]; }
function pushj(j) { stackj[++nj] = j; }
function popj() { return stackj[nj--]; }

function generate_j(n,j) {
  if(verbose) print"Generating rule " n " subrule " j; sjn[n,j] = 0;
  for (k=1; (n,j,k) in rule; ++k) {
    if (rule[n,j,k] == "a" || rule[n,j,k] == "b") {
      if (sn[rule[n,j,k]] == 0) if(verbose) print"Generating " rule[n,j,k];
      s[rule[n,j,k],1] = rule[n,j,k]; sn[rule[n,j,k]] = 1;
    } else {
      if (sn[rule[n,j,k]] == 0) {
        pushk(k); generate(rule[n,j,k]); k = popk();
      }
    }
    if (k == 1) {
      sjn[n,j] = sn[rule[n,j,k]];
      for (q=1; q <= sn[rule[n,j,k]]; ++q) sj[n,j,q] = s[rule[n,j,k],q];
    } else {
      for (m=1; m<=sjn[n,j]; ++m) temp[m] = sj[n,j,m];
      sjn[n,j] = 0;
      for (p=1; p<m; ++p)
      for (q=1; q <= sn[rule[n,j,k]]; ++q) {
        sj[n,j,++sjn[n,j]] = temp[p] s[rule[n,j,k],q]; # Cartesian product (appending) of s[rule[n,j,k]] with sj[n,j] so far
      }
      delete temp;
    }
  }
  if(verbose) print"Done generating rule " n " subrule " j " num:" sjn[n,j];
}

function generate(n) {
  if(verbose) print"Generating " n; sn[n] = 0;
  for (j=1; (n,j,1) in rule; ++j) {
    if (sjn[n,j] == 0) {
      pushj(j); generate_j(n,j); j = popj();
    }
    for (m=1; m<=sjn[n,j]; ++m) {
      s[n,++sn[n]] = sj[n,j,m]; 
      if(verbose) print"  ... " s[n,sn[n]];
    }
  }
  print"Done generating " n " num:" sn[n];
}

/^[0-9]* :/ {
  j = 1; k = 1;
  for (i=3; i<=NF; ++i)
    if ($i == "|") {
      ++j; k = 1;
    } else {
      rule[$1,j,k++] = $i;
      if(verbose) print "Rule_"$1"["j","k-1"]="$i;
    }
}

/^$/ {
  # Build all possibilities as the index set of query.
  generate(0);
  for (m=1; m < sn[0]; ++m) query[s[0,m]] = 1;
}

/^[ab]+$/ {
  if ($0 in query) { ++sum; }
}
END { print sum; }
