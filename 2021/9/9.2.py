def digit(x): return ord(x)-ord('0')

with open("input.txt") as f:
  b=['9'+line.rstrip('\n')+'9' for line in f]
  m=len(b); n=len(b[0])-2
  b.insert(0,'9'*(n+2)); b.append('9'*(n+2))

neighbors=[(-1,0),(1,0),(0,1),(0,-1)]

# Find low points, seed basins
k=0; basin=[[0 for i in range(n+2)] for j in range(m+2)]; size=[0]
for i in range(1,m+1):
  for j in range(1,n+1):
    if all([b[i][j]<b[i+u][j+v] for (u,v) in neighbors]):
      k += 1; basin[i][j] = k; size.append(1)

# Propagate basins by neighbors
finished=False
while not finished:
  finished=True
  for i in range(1,m+1):
    for j in range(1,n+1):
      if digit(b[i][j])==9 or basin[i][j]>0: continue
      for (u,v) in neighbors:
        if basin[i+u][j+v]>0:
          basin[i][j]=basin[i+u][j+v]; size[basin[i][j]] += 1
          finished=False; break

size.sort(reverse=True)
print(size[0] * size[1] * size[2])
