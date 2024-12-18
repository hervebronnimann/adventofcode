import heapq as heap
from collections import defaultdict

grid = [ list(l) for l in open("input.txt").read().strip().split('\n') ]
# grid = [ list(l) for l in open("example.txt").read().strip().split('\n') ]
n = len(grid)
m = len(grid[0])

# 0,1,2,3 -> E,S,W,N
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

# Graph of (i,j,dir) -> (i+di,j+dj,dir): cost=1,  (i,j,dir+/-1): cost=1000
g = defaultdict(list)

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#': continue
        for d in range(4):
            if grid[i++diri[d]][j+dirj[d]] != '#':
                g[(i,j,d)].append((i+diri[d],j+dirj[d],d,1))
            g[(i,j,d)].append((i,j,(d+1)%4,1000))
            g[(i,j,d)].append((i,j,(d+3)%4,1000))

# Graph traversal for distance costs
def dijkstra(src):
    visited = set(src)
    pq = []
    costs = defaultdict(lambda: float('inf'))
    costs[src] = 0
    heap.heappush(pq, (0, src))
    while pq:
        _, node = heap.heappop(pq)
        visited.add(node)
        for i,j,d,cost in g[node]:
            adj = (i,j,d)
            if adj in visited:	continue
            newCost = costs[node] + cost
            if costs[adj] > newCost:
                costs[adj] = newCost
                heap.heappush(pq, (newCost, adj))
    return costs

# In my input I know that S faces East, and arrives at E facing North
dists = dijkstra((n-2,1,0))  # starting East
edists = dijkstra((1,m-2,1)) # starting South
D=dists[(1,m-2,3)]
E=edists[(n-2,1,0)]
print(D,E)

res = 0
for i in range(n):
    for j in range(m):
        for d in range(4):
            if dists[(i,j,d)] + edists[(i,j,(d+2)%4)] == D:
                res += 1; break
print(res)
