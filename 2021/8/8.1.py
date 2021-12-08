import numpy as np

output=[]
with open('input.txt') as f:
  for line in f:
    output.append(line.split('|')[1].split())

print(np.sum([np.sum([1 for s in x if len(s) in [2,3,4,7]]) for x in output]))
