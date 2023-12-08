def score(t):
  w = set([int(x) for x in t[0].split()])
  s = 0
  for z in [int(y) for y in t[1].split()]:
    if z in w: s = 2*s if s>0 else 1
  return s

res = 0
with open("input.txt",'r') as f:
  for s in f:
    s = s.strip().split(":")
    id = int(s[0][5:])
    res += score(s[1].strip().split("|"))

print(res)
