{ h[++k] = $1;
  if (k > 1) last[h[k-1]] = k-1;
}
END{
  while (k < 2020) {
    age = 0;
    if (h[k] in last) age = k - last[h[k]];
    last[h[k]]  = k;
    h[++k] = age;
  }
  print h[2020];
}
