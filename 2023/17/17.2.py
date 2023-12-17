import heapq as heap
from collections import defaultdict

input = open("input.txt",'r').read().strip().split('\n')
n = len(input); m = len(input[0])

# 0,1,2,3 -> E,S,W,N
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

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
            for k in range(4,11):
                edge(i,j,d,k*diri[d],k*dirj[d])
# print(g)

def dijkstra(src):
    visited = set(src)
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[src] = 0
    heap.heappush(pq, (0, src))

    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)

        for i,j,d,cost in g[node]:
            adjNode = (i,j,d)
            if adjNode in visited:	continue

            newCost = nodeCosts[node] + cost
            if nodeCosts[adjNode] > newCost:
                parentsMap[adjNode] = node
                nodeCosts[adjNode] = newCost
                heap.heappush(pq, (newCost, adjNode))
                # print(newCost, adjNode)

    return nodeCosts

dists = dijkstra((0,0,0))
print(min([dists[(n-1,m-1,d)] for d in range(4)]))
