function rot(a) {
  if (a == 90)  { dt = dx; dx = -dy; dy = dt; }
  if (a == 180) { dt = dy; dx = -dx; dy = -dt; }
  if (a == 270) { dt = dx; dx = dy; dy = -dt; }
}
function abs(n) { if (n<0) return -n; return n; }
function P() { print x, y, dx, dy; }
BEGIN { dx = 1; dy = 0; x = 0; y = 0; }
/^N/ { y += $2; P(); }
/^S/ { y -= $2; P(); }
/^E/ { x += $2; P(); }
/^W/ { x -= $2; P(); }
/^L/ { rot($2); P(); }
/^R/ { rot(360-$2); P(); }
/^F/ { x += $2 * dx; y += $2 * dy; P(); }
END { print abs(x) + abs(y); }
