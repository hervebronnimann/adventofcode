function bit(z,m) { return int(z/m)%2; }
function applyMask(x) {
  y = x; k = 0; i = 1;
  m = 34359738368; # 2^35
  while (m > 0) {
    if (mask[i] == "1" && bit(y,m) == 0) { y += m; }
    if (mask[i] == "X") { 
      if (bit(y,m) == 1) y -= m; 
      if (k == 0) { f[k++] = 0; f[k++] = m; }
      else { l = k; for (j = 0; j < l; ++j) { f[k++] = f[j]+m; } }
    }
    m /= 2; ++i;
  }
  return y;
}
/^mask =/ { split($3, mask, ""); }
/^mem/ {
  y = applyMask($2);
  for (j in f) { mem[y+f[j]] = $5; } ## print "mem[" y+f[j] "] = " $5;
  delete f;
}
END {
  sum = 0;
  for (i in mem) sum += mem[i];
  print sum;
}
