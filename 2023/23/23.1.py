from collections import deque

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
        if i+diri[d] not in range(n): continue
        if j+dirj[d] not in range(m): continue
        if input[i+diri[d]][j+dirj[d]] == '#': continue
        L.append((i+diri[d],j+dirj[d]))
    return L

# Compute the junctions, and check that the other parts are linear.
V = [ (0,1,1) ] # , (n,m-2,1) ]
for i in range(n):
    for j in range(m):
        if input[i][j] != '.': continue
        if sum([1 if input[x][y] in '><v^' else 0 for x,y in neighbors(i,j)]) > 1:
            # input[i][j]=chr(ord('A')+len(V)-2)
            for d in range(4):
                if dirc[d] == input[i+diri[d]][j+dirj[d]]: V.append((i,j,d))
        elif sum([1 if input[x][y]=='.><v^' else 0 for x,y in neighbors(i,j)]) > 2:
            print(f'Vertex {i},{j} a junction without clear ><v^ markers')
print(V)
print("\n".join([ "".join(x) for x in input]))

# Going from i,j into direction d, where is the next tile?
def find_next(i,j,d0):
    u,v = i+diri[d0], j+dirj[d0]
    for d in range(4):
        if u+diri[d] not in range(n): continue
        if v+dirj[d] not in range(m): continue
        if input[u+diri[d]][v+dirj[d]] == '#': continue
        if (u+diri[d],v+dirj[d]) == (i,j): continue
        if u+diri[d] == n: return(u,v,d)
        if input[u+diri[d]][v+dirj[d]] == '.': return(u,v,d)
        # For safety, check that we slide in the correct direction
        if dirc[d] == input[u+diri[d]][v+dirj[d]]: return(u,v,d)
    return

# Starting at junction i,j in direction d, where is the next junction, and how far?
input[n-1][m-2] = 'v'
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
graph = {}
for i,j,d in V:
    for e in range(4):
        u,v = i+diri[d], j+dirj[d]
        s,t = u+diri[e], v+dirj[e]
        if (s,t)!=(i,j) and input[s][t] == '.':
            u,v,k = find_next_junction(u,v,e)
            if (i,j) not in graph: graph[(i,j)] = []
            graph[(i,j)].append((u,v,k))
            print(f'From {i},{j} going {d}, {k} steps to {u},{v}')

# Compute distances between the junctions, while obeying
def dfs(i,j):
    if (i,j)==(n-1,m-2):
        return 0
    dist = 0
    for u,v,k in graph[(i,j)]:
        dist = max(dist, dfs(u,v)+k)
    return dist
print(dfs(0,1))
