BEGIN { n = 0; if (size == 0) size = 25; }
{ 
  if (NR > size) {
    found = 0;
    for (i in prev) for (j in prev)
      if (i != j && prev[i] + prev[j] == $1) found = 1;
    if (found == 0) {
      answer = n; print $1;
    }
  }
  input[n] = $1;
  prev[n++ % size] = $1;
}
END {
  for (i = 1; i <= NR; ++i) {
    s = input[i]; m = M = s;
    for (j = i+1; j <= NR ; ++j) {
      x = input[j]; s += x;
      if (x < m) m = x;
      if (x > M) M = x;
      if (s == input[answer]) print m + M;
    }
  }
}
