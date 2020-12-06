BEGIN { n  = 0; m = 0;}
/[a-z]+/ { split($0, chars, ""); for (c in chars) ans[chars[c]] += 1; delete chars; ++m; }
/^$/ { for (c in ans) if (ans[c] == m) ++n; delete ans; m = 0; }
END { for (c in ans) if (ans[c] == m) ++n; print n; }
