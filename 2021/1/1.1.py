with open('1.1.txt') as f:
  n = 0;
  x = int(next(f))
  for line in f:
    y = int(line)
    n += 1 if y > x else 0
    x = y
  print n
