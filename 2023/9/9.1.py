filename = "example.txt"
filename = "input.txt"
input = [ [ int(y) for y in x.split(" ")] for x in open(filename,'r').read().strip().split('\n') ]

def diff(s): return [ s[i] - s[i-1] for i in range(1,len(s))]

res = 0
for x in input:
  y = [x]
  while not all(z == 0 for z in x): 
    x = diff(x)
    y.append(x)
  y[-1].append(0)
  while len(y) > 1:
    z = y[-1][-1]
    y.pop();
    y[-1].append(y[-1][-1]+z)
  print(f"Finally {y[0]}")
  res += y[-1][-1]
print(res)
