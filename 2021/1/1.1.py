import pandas as pd, numpy as np
df = pd.read_csv("input.txt", header=None)
print(sum(np.where(df[0].shift(1) < df[0], 1, 0)))
