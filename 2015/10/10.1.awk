function transform(x) {
  split(x,c,""); k = 1; p = c[1]; y = "";
  for (j=2; j<=length(x); ++j) {
    if (c[j]==p) { ++k; continue; }
    y = y k p;
    p = c[j]; k = 1;
  }
  return y k p;
}
{ input = $1; if (verbose) print transform($1); }
END {
  x = input; for (i=1; i <= 40; ++i) x = transform(x);
  print length(x);
}
