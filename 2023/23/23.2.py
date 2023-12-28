from collections import deque
from copy import deepcopy

input = open("input.txt",'r').read().strip().split('\n')
input = [ list(row) for row in input ]
n = len(input); m = len(input[0])
print(n,m)

# 0,1,2,3 -> R,D,L,U
dir = { 'R':0, 'D':1, 'L':2, 'U':3 }
dirc = [ '>', 'v', '<', '^' ]
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

def neighbors(i,j):
    L = []
    for d in range(4):
        u,v = i+diri[d], j+dirj[d]
        if u not in range(n) or v not in range(m): continue
        if input[u][v] == '#': continue
        L.append((u,v))
    return L

# Compute the junctions, and check that the other parts are linear.
V = [ (0,1,1) ]
for i in range(n):
    for j in range(m):
        if input[i][j] != '.': continue
        if sum([1 if input[x][y] in '><v^' else 0 for x,y in neighbors(i,j)]) > 1:
            # Find all the directions out of the junction
            for d in range(4):
                if dirc[d] == input[i+diri[d]][j+dirj[d]]:
                    V.append((i,j,d))
print(V)

# Going from i,j into direction d, where is the next tile?
def find_next(i,j,d0):
    u,v = i+diri[d0], j+dirj[d0]
    for d in range(4):
        s,t = u+diri[d], v+dirj[d]
        if s not in range(n) or t not in range(m): continue
        if input[s][t] == '#': continue
        if (s,t) == (i,j): continue
        if s == n: return(u,v,d) # final destination!
        if input[s][t] == '.': return(u,v,d) # continue along same path
        # It's a slope: for safety, check that we slide in the correct direction
        if dirc[d] == input[u+diri[d]][v+dirj[d]]: return(u,v,d)
    return None

# Starting at junction i,j in direction d, where is the next junction, and how far?
def find_next_junction(i,j,d):
    k = 1
    while True:
        w = find_next(i,j,d)
        if not w: return (i+diri[d],j+dirj[d],k+1)
        i,j,d = w
        k += 1
        if input[i][j] != '.': break
    return (i+diri[d],j+dirj[d],k+1)

# Construct the graph:
graph = { (i,j):[] for i,j,_ in V }
for i,j,d in V:
    for e in range(4):
        u,v = i+diri[d], j+dirj[d]
        s,t = u+diri[e], v+dirj[e]
        if (s,t)!=(i,j) and input[s][t] == '.':
            u,v,k = find_next_junction(u,v,e)
            graph[(i,j)].append((u,v,k))
            print(f'From {i},{j} going {d}, {k} steps to {u},{v}')

# Compute distances between the junctions, while obeying slopes
def dfs(i,j):
    if (i,j)==(n-1,m-2):
        return 0
    dist = 0
    for u,v,k in graph[(i,j)]:
        dist = max(dist, dfs(u,v)+k)
    return dist
print("Part 1: ", dfs(0,1))

# Undirect the graph:
graph2 = deepcopy(graph)
for i,j in graph:
    for u,v,k in graph[(i,j)]:
        if (u,v)!=(n-1,m-2):
            graph2[(u,v)].append((i,j,k))

# Compute longest simple paths out of each node, in undirected graph
dist = 0; path = []; paths = 0
def dfs2(i,j,k0):
    global dist, path, paths
    if (i,j)==(n-1,m-2):
        dist = max(dist, k0); paths += 1
        return
    path.append((i,j))
    for u,v,k in graph2[(i,j)]:
        if (u,v) in path: continue
        dfs2(u,v,k0+k)
    path.pop()

dfs2(0,1,0)
print("Part 2: ", dist, paths)
