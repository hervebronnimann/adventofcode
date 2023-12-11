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
      # I[(i,j)] = x
      g[(i,j)] = P[x]
      if x=='S': s=(i,j)
      j += 1
    i += 1
# print(s)

d = 1
s10 = s; s1 = add(s,g[s][0])
s20 = s; s2 = add(s,g[s][1])
L = set([s])
while s1 not in L:
  # print(f"{s1} is pipe {I[s1]}; {s2} is pipe {I[s2]}; ")
  if len(g[s1])!=2 or len(g[s2])!=2: print('END OF PIPE'); break
  s12 = add(s1, g[s1][0]); s13 = add(s1, g[s1][1])
  # if s10!=s12 and s10!=s13: print('BAD PIPE'); break
  s1,s10 = (s12 if s12 != s10 else s13, s1); L.add(s10)
  s22 = add(s2, g[s2][0]); s23 = add(s2, g[s2][1]);
  # if s20!=s22 and s20!=s23: print('BAD PIPE'); break
  s2,s20 = (s22 if s22 != s20 else s23, s2); L.add(s20)
  d += 1
print(d if s1 == s2 else d-1)
