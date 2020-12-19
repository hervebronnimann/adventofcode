# A rule is either "[ab]" or "subrule [| subrule]*" with subrule a sequence of integer. Thus complex rules are : j1_k1 j1_k2 ... | j2_k1 j2_k2 ... 
# All match functions match a prefix of tok[l..r], return next l in range [l..r+1] to be checked if prefix match, 0 otherwise.
# If return l==r+1, then all the characters match exactly, with no other characters left to check.

function pushk(j) { stackk[++nk] = k; }
function popk() { return stackk[nk--]; }
function pushj(j) { stackj[++nj] = j; }
function popj() { return stackj[nj--]; }

function generate_j(n,j) {
  if(vverbose) print"Generating rule " n " subrule " j; sjn[n,j] = 0;
  for (k=1; (n,j,k) in rule; ++k) {
    if (rule[n,j,k] == "a" || rule[n,j,k] == "b") {
      if (sn[rule[n,j,k]] == 0) if(vverbose) print"Generating " rule[n,j,k];
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
  if(vverbose) print"Done generating rule " n " subrule " j " num:" sjn[n,j];
}

function generate(n) {
  if(vverbose) print"Generating " n; sn[n] = 0;
  for (j=1; (n,j,1) in rule; ++j) {
    if (sjn[n,j] == 0) {
      pushj(j); generate_j(n,j); j = popj();
    }
    for (m=1; m<=sjn[n,j]; ++m) {
      s[n,++sn[n]] = sj[n,j,m]; 
      if(vverbose) print"  ... " s[n,sn[n]];
    }
  }
  if(vverbose) print"Done generating " n " num:" sn[n];
}

/^[0-9]* :/ {
  j = 1; k = 1;
  for (i=3; i<=NF; ++i)
    if ($i == "|") {
      ++j; k = 1;
    } else {
      rule[$1,j,k++] = $i;
      if(vverbose) print "Rule_"$1"["j","k-1"]="$i;
    }
}

/^$/ {
  # Build all possibilities for 42 and 31 as the index set of query.
  generate(42);
  for (m=1; m <= sn[42]; ++m) { query42[s[42,m]] = 1; if(verbose) print "42: " s[42,m]; }
  generate(31);
  for (m=1; m <= sn[31]; ++m) { query31[s[31,m]] = 1; if(verbose) print "31: " s[31,m]; }
  # CRUCIAL: notice that they ALL have length 8 chars, and there are 128 of each, and 42 and 31 are disjoint.
  LEN = length(s[42,1]);
}

/^[ab]+$/ {
  # 0 : 8 | 11 means that we only need to check chunks of 8 chars in input
  if (length($0) % LEN == 0) {
    match8 = 0; match11 = 0; pattern = "";
    for (i=1; i<=length($0); i+=LEN)
      if (substr($0,i,LEN) in query42) {
        if (match11 == 0) match8 += 1; pattern = pattern " 42";
      } else if (substr($0,i,LEN) in query31) {
        match11 += 1; pattern = pattern " 31";
      } else {
        pattern = pattern " XX";
      }
    if (match8 > match11 && match11 > 0 && match8 + match11 == length($0)/LEN) {
      ++sum; 
      print "Match " match8 " and " match11 " for " $0 " [" pattern"]";
    } else {
      print "Mismatch " match8 " and " match11 " for " $0 " [" pattern"]";
    }
  } else {
    print "No match for irregular length " $0;
  }
}
END { print sum; }
