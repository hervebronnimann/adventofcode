from itertools import permutations
from collections import deque

input = open("input.txt",'r').read().strip().split('\n')
n = len(input); m = len(input[0])

nodes = {}
for i in range(n):
    for j in range(m):
        if input[i][j] in '0123456789':
            nodes[input[i][j]] = (i,j)

diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

def neighbors4(i,j):
    for d in range(4): yield (i+diri[d], j+dirj[d])

def bfs(src,dist):
    visited = set([src])
    pq = deque()
    pq.append((0,src))
    while pq:
        d,(i,j)= pq.popleft()
        for u,v in neighbors4(i,j):
            if input[u][v]=='#': continue
            if (u,v) in visited: continue
            if input[u][v] in nodes: dist[input[u][v]]=d+1
            visited.add((u,v))
            pq.append((d+1,(u,v)))
    return i # float('inf')

# Compute pairwise node distances
dist = {}
for x in nodes:
    dist[x] = {}
    bfs(nodes[x], dist[x])
print(dist)

print("Part 1:", min([sum(dist[p[i-1]][p[i]] for i in range(1,len(nodes))) for p in permutations(nodes) if p[0]=='0']))

print("Part 2:", min([sum(dist[p[i-1]][p[i]] for i in range(1,len(nodes)))+dist[p[-1]][p[0]] for p in permutations(nodes) if p[0]=='0']))
