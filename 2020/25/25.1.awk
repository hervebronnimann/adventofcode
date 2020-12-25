function mult(v,m) { return (v * subject) % m; }
BEGIN { subject = 7; m = 20201227; }
/[0-9]+/ { if (++input == 1) kc = $1; else kd = $1; }
END {
  n = 1; c = 0;  d = 0;
  while (n != kc && n != kd) { n = mult(n,m); ++c; ++d; }
  if (n == kc) { print "c " c " n " n; n = 1; subject = kd; while (c > 0) { n = mult(n,m);  --c; } print "n " n; }
  else if (n == kd) { print "d " d " n " n; n = 1; subject = kc; while (d > 0) { n = mult(n,m);  --d; } print "n " n; } 
}
