from collections import deque
from functools import cache

def popcount(x):
    return bin(x).count("1")

@cache
def grid(x:int,y:int):
    if x<0 or y<0: return '#'
    return '.' if popcount(x*x + 3*x + 2*x*y + y + y*y + input)%2==0 else '#'

diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

# input = 10
# print("\n".join([ "".join([grid(j,i) for j in range(11)]) for i in range(11)]))

# Graph traversal for distance costs
def bfs(src,dst):
    visited = set([src])
    pq = deque()
    pq.append((0,src))
    while pq:
        i,node = pq.popleft()
        # print(i,node)
        for d in range(4):
            adj = (node[0]+dirj[d],node[1]+diri[d])
            if grid(adj[0],adj[1])=='#': continue
            if adj in visited: continue
            if adj == dst: return i+1
            visited.add(adj)
            pq.append((i+1, adj))
    return float('inf')

# input = 10
# print(bfs((1,1),(7,4)))
input = 1362
print(bfs((1,1),(31,39)))
