BEGIN { n = 0; if (size == 0) size = 25; }
{ 
  if (NR > size) {
    found = 0;
    for (i in prev) for (j in prev) if (i != j && prev[i] + prev[j] == $1) found = 1;
    if (found == 0) print $1;
  }
  prev[n++ % size] = $1;
}
