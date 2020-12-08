function loop() { 
  accumulator = 0; ln = 1; while (!(ln in seen) && ln != NR + 1) { accumulator += acc[ln]; seen[ln] = 1; ln = nx[ln]; }
  delete seen; 
  return ln == NR + 1;
}
BEGIN { accumulator = 0; }
/^acc/ { acc[NR] = $2; nx[NR] = NR + 1; }
/^nop/ { acc[NR] = 0; nx[NR] = NR + 1; sw[NR] = NR + $2; nop[NR] = NR; }
/^jmp/ { acc[NR] = 0; nx[NR] = NR + $2; sw[NR] = NR + $2; jmp[NR] = NR; } 
END {
  loop();
  print "Loop detected ending in ", ln ", accumulator = ", accumulator;
  for (n in nop) {
    nx[n] = sw[n]; if (loop()) print "Changing " n " into jmp results in accumulator " accumulator;
    nx[n] = n + 1;
  }
  for (n in jmp) {
    nx[n] = n + 1; if (loop()) print "Changing " n " into nop results in accumulator " accumulator;
    nx[n] = sw[n];
  }
}
