def safe(x : list, d : int):
    for x,y in zip(x,x[1:]):
        if x*d < y*d+1 or x*d > y*d + 3: return 0
    return 1

n = 0
with open("input.txt",'r') as f:
  for s in f:
      x = [int(x) for x in s.split()]
      n = n + safe(x, 1) + safe(x, -1)
print(n)
