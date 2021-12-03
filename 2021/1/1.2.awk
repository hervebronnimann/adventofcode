{ if (NR>4 && $1 > prev[(NR-1)%4]) ++n; prev[NR%4] = $1 }
END { print n; }
