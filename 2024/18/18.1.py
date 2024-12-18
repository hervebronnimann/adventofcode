import heapq as heap
from collections import defaultdict

n,m,N = 7,7,12
input = open("example.txt").read().strip().split('\n')
n,m,N = 71,71,1024
input = open("input.txt").read().strip().split('\n')
grid = [['.' for j in range(m) ] for i in range(n)]
for l in input[0:N]:
    i,j = [ int(x) for x in l.split(',') ]
    grid[i][j] = '#'
print('\n'.join([''.join(l) for l in grid]))

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

g = graph(grid)
dists = dijkstra(g,(0,0))
print(dists[(n-1,m-1)])
