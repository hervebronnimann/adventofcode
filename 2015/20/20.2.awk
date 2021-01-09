BEGIN { max=2000000; input=29000000; }
END {
  for (i=1; i<=max; ++i)
    for (x=i; x<=50*i; x+=i)
      gifts[x] += i;
  for (i=1; i<=max; ++i)
    if (11*gifts[i] >= input) {
      print i; break;
    }
}
