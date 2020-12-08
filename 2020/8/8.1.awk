/^acc/ { acc[NR] = $2; nx[NR] = NR + 1; }
/^nop/ { acc[NR] = 0; nx[NR] = NR + 1; }
/^jmp/ { acc[NR] = 0; nx[NR] = NR + $2; }
END {
  accumulator = 0; ln = 1;
  while (!(ln in seen)) { accumulator += acc[ln]; seen[ln] = 1; ln = nx[ln]; }
  print "Loop detected ending in ", ln ", accumulator = ", accumulator;
}
