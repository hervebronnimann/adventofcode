function f(n) { return n==2 || n==4 || n==3 || n == 7 ? 1 : 0; }
BEGIN { n = 0 }
f(length($12)) { ++n }
f(length($13)) { ++n }
f(length($14)) { ++n }
f(length($15)) { ++n }
END { print n }
