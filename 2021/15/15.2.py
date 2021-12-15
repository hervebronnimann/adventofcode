from collections import defaultdict
import heapq as heap

grid=[]
incr=dict(zip(['1','2','3','4','5','6','7','8','9'],\
              ['2','3','4','5','6','7','8','9','1']))

def neighbors(i,j,m,n): 
  res=[]
  if i>0: res.append((i-1,j))
  if j>0: res.append((i,j-1))
  if i<m-1: res.append((i+1,j))
  if j<n-1: res.append((i,j+1))
  return res

with open('input.txt') as f:
  for l in f:
    grid.append(list(l.strip()))
  m=len(grid); n = len(grid[0])
  def shift(x):
    y=[]
    for z in x: y.append(incr[z])
    return y
  for k in range(4*m):
    grid.append(shift(grid[-m]))
  for k in range(4):
    for i in range(len(grid)):
      grid[i].extend(shift(grid[i][-n:]))

m=len(grid); n=len(grid[0])
print(m,n)

dist=[[n*m*1000 for j in range(n)] for i in range(m)]
dist[0][0]=0

visited=set()
pq=[]
heap.heappush(pq,(0,(0,0)))
while pq:
  _,(i,j) = heap.heappop(pq)
  visited.add((i,j))
  for ni,nj in neighbors(i,j,m,n):
    if (ni,nj) in visited: continue
    newdist = dist[i][j]+int(grid[ni][nj])
    if newdist < dist[ni][nj]:
      dist[ni][nj] = newdist
      heap.heappush(pq,(newdist,(ni,nj)))

print(dist[-1][-1])
