# Symbols in input have been replaced in input2 by `tr AKQJT ZYXWV` so as to be ordered alphabetically
hands = [ x.split(' ') for x in open("input2.txt",'r').read().strip().split('\n') ]

# Do it by hand, counting distinct cards and max count in each hand
# In part 2, we clean up with a simpler `return (-len(s), m)`.
def type(h : str):
  s = set(h)
  m = max([h.count(x) for x in s])
  if len(s) == 1: return 7  # Watch out, there is a hand 'JJJJJ' (one of the Js is a joker!)
  if len(s) == 2: return 6 if m == 4 else 5
  if len(s) == 3: return 4 if m == 3 else 3
  if len(s) == 4: return 2
  return 1

seq = [ (type(x),x,int(v)) for x,v in hands ]
seq.sort()

res = 0
for i,s in enumerate(seq):
  res += s[2] * (i+1)
print(res)
