import pandas as pd, numpy as np
df = pd.read_csv("1.1.txt", header=None)
print(sum(np.where(df[0].shift(3) < df[0], 1, 0)))
return

with open('1.1.txt') as f:
  m = 0; n = 0; x = {}
  for line in f:
    m += 1
    x[m%4] = int(line)
    n += 1 if m>3 and x[m%4] > x[(m-3)%4] else 0
  print n
