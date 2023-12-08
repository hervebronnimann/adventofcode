from collections import defaultdict 

m = {}
with open("input.txt",'r') as f:
  source = ""
  dest = ""
  for s in f:
    s = s.strip()
    if s.startswith("seeds:"):
      seeds = [ int(x) for x in s[6:].split() ]
    elif "map" in s:
      source, _, dest = s.split()[0].split("-")
      m[(source,dest)] = []
    elif len(s) > 0:
      d0, s0, l = [ int(x) for x in s.split() ]
      m[(source,dest)].append( (d0,s0,l) )

def compute(ml: list, x: int):
  for (d,s,l) in ml:
    if x >= s and x < s+l: return d + x-s
  return x

print(m)
seq = [ "soil", "fertilizer", "water", "light", "temperature", "humidity", "location" ]

res = -1

for s in seeds:
  src = "seed"
  for dst in seq:
    print(f"{src} {s}")
    s = compute(m[(src,dst)], s)
    src = dst
  print(f"location {s}")
  res = min(res,s) if res > 0 else s

print(res)
