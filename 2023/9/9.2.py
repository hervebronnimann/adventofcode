input = [ [ int(y) for y in x.split(" ")] for x in open("input.txt",'r').read().strip().split('\n') ]

def diff(s): return [ s[i] - s[i-1] for i in range(1,len(s))]

res = 0
for x in input:
  y = [x]
  while any(y[-1]):
    y.append(diff(y[-1]))
  y[-1].append(0)
  while len(y) > 1:
    z = y.pop()[0]
    y[-1].insert(0,y[-1][0]-z)
  res += y[0][0]
print(res)
