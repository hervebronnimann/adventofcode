BEGIN { pos = 0; if (right == 0) right = 3; if (down == 0) down = 1; n = 0; }
{ if ((NR-1) % down == 0) { if (substr($0,pos+1,1) == "#") ++n; pos += right; pos %= length($0); } }
END { print "(", right, down, ") = ", n; }
