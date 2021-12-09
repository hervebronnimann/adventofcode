def digit(x): return ord(x)-ord('0')

with open("input.txt") as f:
  m=0; b={}
  for line in f: n=len(line); m+=1; b[m]='9'+line.rstrip('\n')+'9'
  b[0]='9'*(n+2); b[m+1]='9'*(n+2)

# Find low points, seed basins
k=0; basin=[[0 for i in range(n+2)] for j in range(m+2)]; size=[0]
for i in range(1,m+1):
  for j in range(1,n+1):
    if b[i][j]<b[i+1][j] and b[i][j]<b[i-1][j] and b[i][j]<b[i][j+1] and b[i][j]<b[i][j-1]:
      # print("Low point %s at [%d,%d]" % (b[i][j],i,j))
      k += 1; basin[i][j] = k; size.append(1)

# Propagate basins by neighbors
finished=False
while not finished:
  finished=True
  for i in range(1,m+1):
    for j in range(1,n+1):
      if digit(b[i][j])==9 or basin[i][j]>0: continue
      if   basin[i+1][j]>0: basin[i][j]=basin[i+1][j]; size[basin[i][j]] += 1; finished=False
      elif basin[i-1][j]>0: basin[i][j]=basin[i-1][j]; size[basin[i][j]] += 1; finished=False
      elif basin[i][j+1]>0: basin[i][j]=basin[i][j+1]; size[basin[i][j]] += 1; finished=False
      elif basin[i][j-1]>0: basin[i][j]=basin[i][j-1]; size[basin[i][j]] += 1; finished=False

size.sort(reverse=True)
print(size[0] * size[1] * size[2])
