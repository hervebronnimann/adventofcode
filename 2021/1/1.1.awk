{ if (NR>1 && $1 > prev) ++n; prev = $1}
END { print n; }
