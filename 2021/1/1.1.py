import pandas as pd, numpy as np
df = pd.read_csv("1.1.txt", header=None)
print(sum(np.where(df[0].shift(1) < df[0], 1, 0)))
exit

with open('1.1.txt') as f:
  n = 0;
  x = int(next(f))
  for line in f:
    y = int(line)
    n += 1 if y > x else 0
    x = y
  print n
