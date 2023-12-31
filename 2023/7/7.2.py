# Symbols in input have been replaced in input2 by `tr AKQJT ZYXWV` so as to be ordered alphabetically
hands = [ x.split(" ") for x in open("input2.txt",'r').read().strip().split('\n') ]

# Clean up of part 1, using jokers to go to the card with the largest count.
def type(h : str):
  s = set(h); s.discard('W'); j = h.count('W')
  if len(s) == 0: return (-1,5)  # All aces!
  m = max([h.count(x) for x in s]) + j
  return (-len(s), m)

seq = [ (type(x),x.replace('W','*'),int(v)) for x,v in hands ]
seq.sort()

res = 0
for i in range(len(seq)):
  res += seq[i][2] * (i+1)
print(res)
