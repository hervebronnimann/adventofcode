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

# Find starting point, should be in the middle
for i in range(n):
    for j in range(m):
        if input[i][j] == 'S': i0,j0 = i,j
print(i0,j0, i0 == (n-1)/2, j0 == (m-1)/2)

for i in range(n):
    for j in range(m):
        if input[i][j] == '#': continue
        g[(i,j)] = list()
        # Add edges between sandboxes inside the grid
        for d in range(4):
            i2 = i+diri[d]; j2 = j+dirj[d]
            if i2 not in range(n): continue
            if j2 not in range(m): continue
            if input[i2][j2] == '#': continue
            g[(i,j)].append((i2,j2))

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
c = dijkstra((i0,j0))

c0 = dijkstra((0,0))
c1 = dijkstra((0,m-1))
c2 = dijkstra((n-1,m-1))
c3 = dijkstra((n-1,0))

ca = dijkstra((i0,0))
cb = dijkstra((0,j0))
cc = dijkstra((i0,m-1))
cd = dijkstra((n-1,j0))

D = 115
N = (D-i0) // n; q = D % n
print(N, q, q == i0, N%2==0, i0%2 == 1, q-1 == (n-3)/2, n+q-1 == (3*n-3)/2)

def within(d,costs):
    return sum([1 if costs[node]<=d and costs[node]%2==d%2 else 0 for node in costs])

E = within(5*n,c)
O = within(5*n+1,c)
print(E,O)

A = within(n+q-1,c0) + within(n+q-1,c1) + within(n+q-1,c2) + within(n+q-1,c3)
B = within(q-1,c0) + within(q-1,c1) + within(q-1,c2) + within(q-1,c3)
T = within(n,ca) + within(n,cb) + within(n,cc) + within(n,cd)
print(A,B,T)

print((N-1)*(N-1)* O + N*N*E + (N-1)*A + N*B + T)
