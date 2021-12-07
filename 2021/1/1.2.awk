{ if (NR>3 && $1 > prev[(NR-3)%4]) ++n; prev[NR%4] = $1 }
END { print n; }
