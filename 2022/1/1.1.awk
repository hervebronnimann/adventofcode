BEGIN { sum = 0; max = 0; }
/^$/ { if (sum > max) max = sum; sum = 0; next; }
{ sum = sum + $1; }
END { print max }
