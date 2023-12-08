from collections import defaultdict 

def color(s : str):
  s = s.split()
  return (s[1], int(s[0]))

def valid(s : str):
  t = defaultdict(lambda:0, [ color(x) for x in s.split(",")])
  # print(t)
  return 1 if t["red"] <= 12 and t["green"] <= 13 and t["blue"] <= 14 else 0

res = 0
with open("input.txt",'r') as f:
  for s in f:
    s = s.strip().split(":")
    id = int(s[0][5:])
    a = [ valid(x) for x in s[1].strip().split(";") ]
    if 0 in a: continue
    res += id
print(res)
