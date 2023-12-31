import math

input = open("input.txt",'r').read().strip().split('\n')

left = {}
right = {}
start = set()
end = set()
for x in input[2:]:
  x,l,r = x.split()
  left[x] = l
  right[x] = r
  if x[2]=='A': start.add(x)
  if x[2]=='Z': end.add(x)

ins = input[0]

steps = {}
for s in start:
  x = s
  st = 0
  while x not in end:
    for p in ins:
      st += 1
      x = left[x] if p == "L" else right[x]
      if x in end: break
    steps[s] = st

G = 1
for x in steps.values():
  print(G,x)
  G = G * x // abs(math.gcd(G, x))

print(G)
