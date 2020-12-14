function bit(z,m) { return int(z/m)%2; }
function applyMask(x) {
  y = x; i = 1;
  m = 34359738368; # 2^35
  while (m > 0) {
    if (mask[i] == "0" && (bit(y,m) == 1)) y -= m;
    if (mask[i] == "1" && (bit(y,m) == 0)) y += m;
    m /= 2; ++i;
  }
  return y;
}
/^mask =/ { split($3, mask, ""); }
/^mem/ { mem[$2] = applyMask($5); }
END {
  sum = 0;
  for (i in mem) sum += mem[i];
  print sum;
}
