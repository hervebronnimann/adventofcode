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

# Graph traversal for distance costs
def bfs(src,D):
    visited = set([src])
    soln = set([src])
    pq = deque()
    pq.append((0,src))
    while pq:
        i,node = pq.popleft()
        if i>D+2: break
        for d in range(4):
            adj = (node[0]+dirj[d],node[1]+diri[d])
            if grid(adj[0],adj[1])=='#': continue
            if adj in visited: continue
            visited.add(adj)
            pq.append((i+1, adj))
            if i+1<=D: soln.add(adj)
    M = max([m for m,_ in soln])
    N = max([n for _,n in soln])
    print("\n".join([ "".join(['O' if (j,i) in soln else grid(j,i) for j in range(M+2)]) for i in range(N+2)]))
    print()
    return len(soln)

input = 1362
print(f"{bfs((1,1),50)} steps/points")
