# A rule is either "[ab]" or "subrule [| subrule]*" with subrule a sequence of integer. Thus complex rules are : j1_k1 j1_k2 ... | j2_k1 j2_k2 ... 
# All match functions match a prefix of tok[l..r], return next l in range [l..r+1] to be checked if prefix match, 0 otherwise.
# If return l==r+1, then all the characters match exactly, with no other characters left to check.

function pushk(j) { stackk[++nk] = k; }
function popk() { return stackk[nk--]; }
function pushj(j) { stackj[++nj] = j; }
function popj() { return stackj[nj--]; }

function rmatch_jk(n,l,r,j,k) {  # prefix of tok[l..r] match rule n, subrule j, element k
  if (rule[n,j,k] == "a" || rule[n,j,k] == "b") {
    if(verbose) print " ... trying "$0"["l","r"] rule_"n"["j","k"] = "rule[n,j,k]
    if (l <= r && tok[l] == rule[n,j,k]) return l+1; else return 0;
  }
  if (l <= r) return rmatch(rule[n,j,k],l,r,0);
  return 0;
}
function rmatch_j(n,l,r,j) {  # prefix of tok[l..r] match rule n, subrule j
  if(verbose) print " ... match "$0"["l","r"]:"
  for (k=1; (n,j,k) in rule; ++k) {
    if(verbose) print " ... trying "$0"["l","r"] rule_"n"["j","k"]"
    pushk(k); l3 = rmatch_jk(n,l,r,j,k); k = popk();
    if (l3 == 0) return 0;
    if(verbose) print " ... match "$0"["l","r"] rule_"n"["j","k"] continues at "l3;
    l = l3;
  }
  return l;
}
function rmatch(n,l,r,exact) {  # prefix or full string of tok[l..r] match rule n
  if(verbose) print " ... match "$0"["l","r"]:"
  for (j=1; (n,j,1) in rule; ++j) {
    if(verbose) print " ... trying "$0"["l","r"] rule_"n"["j"]"
    pushj(j); l2 = rmatch_j(n,l,r,j); j = popj();
    if (l2 > 0) {
      if(verbose) print " ... match "$0"["l","r"] rule_"n"["j"] ends at "l2;
      if (exact==0 || l2 == r+1) return l2;
    }
  }
  return 0;
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
/^[ab]+$/ {
  split($0, tok, "");
  r1 = length(tok);
  l1 = rmatch(0, 1, r1,1);
  if (l1 == r1+1) { ++sum; print $0 " matches rule 0"; }
  else { # debugging...
    print "No match "$0"[1,"r1"] ends at "l1;
  }
}
END { print sum; }
