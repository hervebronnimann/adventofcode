def safe(x : list, d : int):
    for x,y in zip(x,x[1:]):
        if x*d < y*d+1 or x*d > y*d + 3: return 0
    return 1

def safe1(x : list, d : int):
    if safe(x,d): return 1
    for i in range(len(x)):
        y = x[0:i]
        y.extend(x[i+1:])
        if safe(y,d): return 1
    return 0

n = 0
with open("input.txt",'r') as f:
  for s in f:
      x = [int(x) for x in s.split()]
      n = n + safe1(x, 1) + safe1(x, -1)
print(n)
