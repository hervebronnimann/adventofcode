import heapq as heap
from collections import defaultdict

input = open("input.txt",'r').read().strip().split('\n')
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
# Extract number of nodes at given distance from the center, with same parity:
c = dijkstra((i0,j0))
print([sum([1 if c[node]<=d and c[node]%2==d%2 else 0 for node in c]) for d in range(n)])

# We have D steps, and N copies of the grid plus the leftovers to reach the rightmost point.
# Because the leftover q is the same as the coordinate of the center, the last point we reach
# on each axis is on the boundary of the grid!
D = 26501365
N = (D-i0) // n; q = D % n; w = (n-1)//2

# All these assumptions should be true:
print(N, q, q == w, n == 2*w+1, N%2==0, i0%2 == 1, n-w-2 == (n-3)/2, 2*n-w-2 == (3*n-3)/2)

# Because once we replicate the grid, we have a pattern. It looks like this (here N=6):
#
#             B T B               T      /`    B   +
#           B A E A B                   /  `       |
#         B A E O E A B                /    `      ``
#       B A E O E O E A B             |      |     | ``
#     B A E O E O E O E A B           +------+     +---`--+
#   B A E O E O E O E O E A B
#   T E O E O E O E O E O E T
#   B A E O E O E O E O E A B
#     B A E O E O E O E A B                    A   +---`
#       B A E O E O E A B                          |    `
#         B A E O E A B                            |     `
#           B A E A B                              |      |
#             B T B                                +------+
#
# The center is O because D is odd, and then and since n==m is odd, we
# alternate the leftover steps between odd/even on the inside, in a checkerboard,
# and on the outer edges we have A B and T which have different values of
# leftover steps.  Because N is even, the number of E squares is N^2, and
# there are (N-1)^2 copies of O (this can most easily be seen by looking at
# a 45 degree angle).  The number of steps to reach the bottom-left corner of A
# is (N-2)*n to reach the last O on the axis, plus 2*(w+1), and so there are only
#   D - (N-2)*n -2*(w+1) = N*n + w - (N-2)*n -2*w - 2 = 2*n - w - 2
# Likewise for B, the only difference is to reach E instead of O, and so n - w - 2.
# To reach the first point in T, it takes (N-1)*n+w+1 steps, and so this leaves
#   D - (N-1)*n - w - 1 = N*n + w - (N-1)*n - w - 1 = n - 1
# Also A B and T have their four rotations, so the number of T1 is 1, the number
# of A1 is (N-1), and the number of B1 is N, and same from A2,A3,A4 etc.

c0 = dijkstra((0,0))
c1 = dijkstra((0,m-1))
c2 = dijkstra((n-1,m-1))
c3 = dijkstra((n-1,0))

ca = dijkstra((i0,0))
cb = dijkstra((0,j0))
cc = dijkstra((i0,m-1))
cd = dijkstra((n-1,j0))

def within(d,costs):
    return sum([1 if costs[node]<=d and costs[node]%2==d%2 else 0 for node in costs])

E = within(2*n,c)
O = within(2*n+1,c)
print(E,O)

A = within(2*n-w-2,c0) + within(2*n-w-2,c1) + within(2*n-w-2,c2) + within(2*n-w-2,c3)
B = within(n-w-2,c0) + within(n-w-2,c1) + within(n-w-2,c2) + within(n-w-2,c3)
T = within(n-1,ca) + within(n-1,cb) + within(n-1,cc) + within(n-1,cd)
print(A,B,T)

print((N-1)*(N-1)* O + N*N*E + (N-1)*A + N*B + T)
