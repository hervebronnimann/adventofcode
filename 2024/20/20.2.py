import heapq as heap
from collections import defaultdict

grid = open("input.txt").read().strip().split('\n')
grid = [ list(l) for l in grid ]
n,m = len(grid),len(grid[0])
si,sj,ei,ej = -1,-1,-1,-1
for i in range(n):
  for j in range(m):
    if grid[i][j] == 'S': si,sj = i,j
    if grid[i][j] == 'E': ei,ej = i,j
grid[si][sj] = '.'
grid[ei][ej] = '.'

# 0,1,2,3 -> E,S,W,N
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

# Graph of (i,j) -> (i+di,j+dj): cost=1
def graph(grid):
    g = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#': continue
            for d in range(4):
                if i++diri[d] not in range(n): continue
                if j++dirj[d] not in range(m): continue
                if grid[i++diri[d]][j+dirj[d]] != '#':
                    g[(i,j)].append((i+diri[d],j+dirj[d],1))
    return g

# Graph traversal for distance costs
def dijkstra(g,src):
    visited = set(src)
    pq = []
    costs = defaultdict(lambda: float('inf'))
    costs[src] = 0
    heap.heappush(pq, (0, src))
    while pq:
        _, node = heap.heappop(pq)
        visited.add(node)
        for i,j,cost in g[node]:
            adj = (i,j)
            if adj in visited:	continue
            newCost = costs[node] + cost
            if costs[adj] > newCost:
                costs[adj] = newCost
                heap.heappush(pq, (newCost, adj))
    return costs

g0 = graph(grid)
dist = dijkstra(g0,(si,sj))
dist0 = dist[(ei,ej)]
saves = defaultdict(int)
edist = dijkstra(g0,(ei,ej))
print('\n'.join([''.join(l) for l in grid]))
print(si,sj,ei,ej)
print(dist0)
for i in range(1,n-1):
  for j in range(1,m-1):
    if grid[i][j] == '#': continue
    for i2 in range(1,n-1):
      for j2 in range(1,m-1):
        if grid[i2][j2] == '#': continue
        d = abs(i2-i)+abs(j2-j)
        if d > 20: continue
        shortcut = dist[(i,j)] + d + edist[(i2,j2)]
        if shortcut < dist0: saves[dist0 - shortcut] += 1
print(saves)
print([(saves[i],i) for i in sorted(saves.keys())])
print(sum([saves[i] for i in sorted(saves.keys()) if i >= 100]))
