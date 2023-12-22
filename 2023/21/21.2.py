import heapq as heap
from collections import defaultdict

input = open("example.txt",'r').read().strip().split('\n')
n = len(input); m = len(input[0])
print(n,m)

# 0,1,2,3 -> R,D,L,U
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

# Graph of (i,j,dir) -> (i+di,j+dj,dir+/-1): cost
g = {}

# Find starting point
for i in range(n):
    for j in range(m):
        if input[i][j] == 'S': i0,j0 = i,j
print(i0,j0)

# Create graph of 3x3 copies of the grid, centered at (i0,j0)
k = 10
def node(i,j):
    for x in range(-k,k+1):
        for y in range(-k,k+1):
            g[(i+x*n,j+y*m)] = list()

def edge(i,j,d):
    for x in range(-k,k+1):
        for y in range(-k,k+1):
            i2,j2 = (i+x*n+diri[d],j+y*m+dirj[d])
            if (i2,j2) in g:
                g[(i+x*n,j+y*m)].append((i2,j2))

for i in range(n):
    for j in range(m):
        if input[i][j] == '#': continue
        node(i,j)

for i in range(n):
    for j in range(m):
        if input[i][j] == '#': continue
        # Stitch the edges of the grid
        if i == 0: edge(i,j,3)
        if i == n-1: edge(i,j,1)
        if j == 0: edge(i,j,2)
        if j == m-1: edge(i,j,0)
        # Add edges between sandboxes inside the grid
        for d in range(4):
            if i+diri[d] not in range(n): continue
            if j+dirj[d] not in range(m): continue
            if input[i+diri[d]][j+dirj[d]] == '#': continue
            edge(i,j,d)

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

# From now on we must assume that n==m, and that n is odd, or else this won't work.
# Extract number of nodes at given distance from each 4 corners, with same parity:
costs = dijkstra((i0,j0))  # ; print(costs)
c = []
for d in range((k+1)*n+1):
    c.append(sum([1 if costs[(x,y)]<=d and costs[(x,y)]%2==d%2 else 0 for x,y in costs]))
print([(i,x) for i,x in enumerate(c)])

x = 26501365
p = x // n; q = x % n
print(p,q,c[q],c[n+q])

# Count per vertical slices of n nodes:
#
# 0 .................... (p*n,0) .. q
# .      .                .    /
# .      .                * /
# .      .               /
# .      .              /
# . ..(p-1)*n,0) . .. q
#
#
res = 0
while p > 0:
    res += c[q] + c[n+q]
    res += (c[2*n-1] + c[2*n]) * ((p-1)//2) + (c[2*n-1] if (p-1)%2 == 1 else 0)
    p -= 1
res += c[q]

# We're double counting the reachable ones on the axes, there are x//2 of these
print(res - (x//2 * 4))
