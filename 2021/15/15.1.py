grid=[]
with open('input.txt') as f:
  for l in f:
    grid.append(list(l.strip()))
  m=len(grid); n = len(grid[0])

m=len(grid); n=len(grid[0])

low=[[0 for j in range(n)] for i in range(m)]
for i in range(m):
  for j in range(n):
    low[i][j]= int(grid[i][j]) + \
      min(low[i-1][j] if i>0 else 1000000,\
          low[i][j-1] if j>0 else 1000000,\
          0 if i==0 and j==0 else 1000000)

print(low[-1][-1]-int(grid[0][0]))

