import re
from collections import defaultdict 

def color(s : str):
  s = s.split()
  return (s[1], int(s[0]))

def valid(s : str):
  t = defaultdict(lambda:0, [ color(x) for x in s.split(",")])
  return (t["red"], t["green"], t["blue"])

res = 0
with open("input.txt",'r') as f:
  for s in f:
    s = s.strip().split(":")
    id = int(s[0][5:])
    a = [ valid(x) for x in s[1].strip().split(";") ]
    r = max([r for (r,_,_) in a])
    g = max([g for (_,g,_) in a])
    b = max([b for (_,_,b) in a])
    # print(id, r, g, b)
    res += r*g*b
print(res)
