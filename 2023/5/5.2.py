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
      m[(source,dest)].append( (s0,l,d0) )

seq = [ "soil", "fertilizer", "water", "light", "temperature", "humidity", "location" ]
src = "seed"
for dst in seq:
  m[(src,dst)].sort()
  src = dst

def shft(x,y,s,d):
  """ Return the image of [x,y) shifting from s to d. """
  return (d+x-s,d+y-s)

def compute(ml:list, i:int, x:int, y:int):
  """ Return the image of [x,y) shifting from the sequence of ml[i:], which is a sequence of mappings from [s,s+l) to [d,d+l). """
  if i == len(ml):
    return [(x,y)]
  (s,l,d) = ml[i]
  if y <= s:
    return [(x,y)] 
  if y <= s+l:
    if x < s:
      return [(x,s),shft(s,y,s,d)]
    return [shft(x,y,s,d)]
  # s+l < y
  if s+l <= x:
    return compute(ml,i+1,x,y)
  if s <= x:
    return [shft(x,s+l,s,d)] + compute(ml,i+1,s+l,y)
  return [(x,s),shft(s,s+l,s,d)] + compute(ml,i+1,s+l,y)

print(m)

src = "seed"
res = -1
n = 0

for i in range(len(seeds)//2):
  src = "seed"
  l = [(seeds[2*i],seeds[2*i]+seeds[2*i+1])]
  #print(l)
  for dst in seq:
    p = []
    for (s1,s2) in l:
      p += compute(m[(src,dst)], 0, s1,s2)
    src = dst
    l = p
    #print(f"After {dst}, {len(l)}")
    n += len(l)
  for s,_ in l:
    res = min(res,s) if res > 0 else s

print(res, n)
