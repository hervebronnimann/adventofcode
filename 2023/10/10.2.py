N = (-1,0)
E = (0,1)
S = (1,0)
W = (0,-1)

# in this problem S is a N/S pipe (verified manually)
P = { '|':[N,S], '-':[E,W], 'L':[N,E], 'J':[N,W], '7':[S,W], 'F':[S,E], '.':[], 'S':[N,S] }

def add(x,y): return (x[0]+y[0],x[1]+y[1])

g = {}; I = {}
with open("input.txt",'r') as f:
  i = 0
  for y in f:
    j = 0
    y = y.strip()
    for x in y:
      I[(i,j)] = x
      g[(i,j)] = P[x]
      if x=='S': s=(i,j)
      j += 1
    i += 1
m = i; n = j
# print(s, m, n)

d = 1
s10 = s; s1 = add(s,g[s][0])
L = set([s])
while s1 != s:
  s12 = add(s1, g[s1][0]); s13 = add(s1, g[s1][1])
  s1,s10 = (s12 if s12 != s10 else s13, s1); L.add(s10)

output = ""
inside = 0; res = 0
for i in range(m):
  for j in range(n):
    if (i,j) in L:
      if I[(i,j)] not in ['-','J','L']: inside = 1-inside
      output += I[(i,j)]
    elif inside:
      output += 'I'
      res += 1
    else:
      output += 'O'
  output += "\n"
# print(output)
print(res)
