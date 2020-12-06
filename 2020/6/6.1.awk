BEGIN { n  = 0; }
/[a-z]+/ { split($0, chars, ""); for (c in chars) ans[chars[c]] = 1; delete chars; }
/^$/ { n += length(ans); delete ans; }
END { print n + length(ans); }
