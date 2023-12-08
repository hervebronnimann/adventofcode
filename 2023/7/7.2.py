def type(h : str):
  s = set(h); s.discard('W'); j = h.count('W')
  if len(s) == 0: return -1
  m = max([h.count(x) for x in s])+j
  return (-len(s), m)

def type(h : str):
  s = set(h); s.discard('W'); j = h.count('W')
  if len(s) == 0: return 7
  m = [h.count(x) for x in s]
  m = max(c) ; c.remove(m);  c.append(m+j)
  if len(s) == 1: return 7
  if len(s) == 2: return 6 if max(c) == 4 else 5
  if len(s) == 3: return 4 if max(c) == 3 else 3
  if len(s) == 4: return 2
  return 1

#hands = [ x.split(" ") for x in open("example2.txt",'r').read().strip().split('\n') ]
hands = [ x.split(" ") for x in open("input2.txt",'r').read().strip().split('\n') ]
seq = [ (type(x),x.replace('W','*'),int(v)) for x,v in hands ]
seq.sort()
print(seq)

res = 0
for i in range(len(seq)):
  res += seq[i][2] * (i+1)
print(res)
