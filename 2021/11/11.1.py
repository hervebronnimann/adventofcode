def digit(x): return ord(x)-ord('0')

with open("input.txt") as f:
  b=[[digit(x) for x in line.rstrip('\n')] for line in f]

print(b)

neighbors=[(i,j) for i in [-1,0,1] for j in [-1,0,1] if i!=0 or j!=0]
grid=[(i,j) for i in range(10) for j in range(10)]

def flash(b,s,i,j):
  for u,v in neighbors:
    if i+u<0 or i+u>9 or j+v<0 or j+v>9: continue
    b[i+u][j+v] += 1
    if b[i+u][j+v]==10: s.add( (i+u,j+v) )

flashes = 0
for iter in range(100):
  s=set({})
  for i,j in grid:
    b[i][j]+=1
    if b[i][j]==10: s.add( (i,j) )
  f = len(s)
  while True:
    s2=set({})
    for i,j in s: flash(b,s2,i,j)
    if len(s2)==0: break
    f += len(s2); s=s2
  for i,j in grid:
    if b[i][j]>9: b[i][j]=0
  print("Iteration %d: %d flashes" % (iter,f))
  flashes += f

print(flashes)
