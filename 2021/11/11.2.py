neighbors=[(i,j) for i in [-1,0,1] for j in [-1,0,1] if i!=0 or j!=0]
def grid(m,n): return [(i,j) for i in range(n) for j in range(m)]
def valid(i,j,b): return i>=0 and i<len(b) and j>=0 and j<len(b[0])

with open("input.txt") as f:
  b=[[ord(x)-ord('0') for x in line.rstrip('\n')] for line in f]

def flash(i,j,b):
  if b[i][j]!=10: return 0
  for u,v in neighbors:
    if valid(i+u,j+v,b) and b[i+u][j+v]<10:
      b[i+u][j+v] += 1
  b[i][j] = 99  # To prevent flashing twice
  return 1

g=grid(len(b),len(b[0]))
it=0
while True:
  it += 1
  for i,j in g: b[i][j]+=1
  while True:
     if sum([flash(i,j,b) for i,j in g])==0: break
  for i,j in g:
    if b[i][j]>9: b[i][j]=0
  if all([b[i][j]==0 for i,j in g]): break

print(it)
