BEGIN { sum = 0; max = 0; max2 = 0; max3 = 0; }
/^$/ {
  if (sum > max3) max3 = sum;
  if (max3 > max2) { tmp = max2; max2 = max3; max3 = tmp; }
  if (max2 > max) { tmp = max; max = max2; max2 = tmp; }
  sum = 0; next;
}
{ sum = sum + $1; }
END { print max + max2 + max3 }
