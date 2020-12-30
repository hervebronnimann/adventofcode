# A nice string is one with all of the following properties:
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
BEGIN { res = 0; }
{ split($1,c,""); 
  found1 = 0; found2 = 0;
  idx[c[1] c[2]] = 1;
  for (i=3; i <= length($1); ++i) {
    s = c[i-1] c[i];
    if (s in idx && idx[s] < i-2) found1 = 1;
    if (c[i-2] == c[i]) found2 = 1;
    if (!(s in idx)) idx[s] = i-1;
  }
  if (found1 && found2) ++res;
  delete idx;
}
END { print res; }
