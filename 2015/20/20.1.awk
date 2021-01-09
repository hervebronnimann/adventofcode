BEGIN { max=3000000; input=29000000; }
END {
  for (i=1; i<=max; ++i)
    for (x=i; x<=max; x+=i)
      gifts[x] += i;
  for (i=1; i<=max; ++i)
    if (10*gifts[i] >= input) {
      print i; break;
    }
}
