import heapq as heap
from collections import defaultdict

input = open("input.txt",'r').read().strip().split('\n')
n = len(input); m = len(input[0])

# 0,1,2,3 -> E,S,W,N
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

# Graph of (i,j,dir) -> (i+di,j+dj,dir+/-1): cost
g = {}

def edge(i,j,d,di,dj):
    if i+di < 0 or i+di >= n: return
    if j+dj < 0 or j+dj >= m: return
    cost = 0
    if dj>0: cost = sum([int(input[i][j+x+1]) for x in range(dj)])
    if dj<0: cost = sum([int(input[i][j-x-1]) for x in range(-dj)])
    if di>0: cost = sum([int(input[i+x+1][j]) for x in range(di)])
    if di<0: cost = sum([int(input[i-x-1][j]) for x in range(-di)])
    g[(i,j,d)].append((i+di,j+dj,(d+1)%4,cost))
    g[(i,j,d)].append((i+di,j+dj,(d+3)%4,cost))

for i in range(n):
    for j in range(m):
        for d in range(4):
            g[(i,j,d)] = list()
            edge(i,j,d,1*diri[d],1*dirj[d])
            edge(i,j,d,2*diri[d],2*dirj[d])
            edge(i,j,d,3*diri[d],3*dirj[d])

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

dists = dijkstra((0,0,0))
print(min([dists[(n-1,m-1,d)] for d in range(4)]))
