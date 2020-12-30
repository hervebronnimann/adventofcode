# A nice string is one with all of the following properties:
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
BEGIN { res = 0; vowels["a"] = vowels["e"] = vowels["i"] = vowels["o"] = vowels["u"] = 1; }
{ split($1,c,""); 
  vows = 0; for (i in c) if (c[i] in vowels) ++vows;
  double = 0; for (i=1; i<length($1); ++i) if (c[i]==c[i+1]) double = 1;
print 
}
/ab/ { next; }
/cd/ { next; }
/pq/ { next; }
/xy/ { next; }
{ if (vows >= 3 && double) ++res; }
END { print res; }
