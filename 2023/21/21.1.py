import heapq as heap
from collections import defaultdict

input = open("input.txt",'r').read().strip().split('\n')
n = len(input); m = len(input[0])
print(n,m)

# 0,1,2,3 -> R,D,L,U
dir = { 'R':0, 'D':1, 'L':2, 'U':3 }
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

# Graph of (i,j,dir) -> (i+di,j+dj,dir+/-1): cost
g = {}

for i in range(n):
    for j in range(m):
        if input[i][j] == '#': continue
        if input[i][j] == 'S': i0,j0 = i,j
        g[(i,j)] = list()
        for d in range(4):
            if not i+diri[d] in range(n): continue
            if not j+dirj[d] in range(m): continue
            if input[i+diri[d]][j+dirj[d]] == '#': continue
            g[(i,j)].append((i+diri[d],j+dirj[d]))

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
        for i,j in g[node]:
            adj = (i,j)
            if adj in visited:	continue
            newCost = costs[node] + 1
            if costs[adj] > newCost:
                costs[adj] = newCost
                heap.heappush(pq, (newCost, adj))
    return costs

c = dijkstra((i0,j0))
print(sum([1 for node in c if c[node]<=64 and c[node]%2==0]))
