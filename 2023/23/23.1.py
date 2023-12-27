from collections import deque

input = open("example.txt",'r').read().strip().split('\n')
input = [ list(row) for row in input ]
n = len(input); m = len(input[0])

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
    return None

# Starting at junction i,j in direction d, where is the next junction, and how far?
def find_next_junction(i,j,d):
    k = 1
    while True:
        w = find_next(i,j,d)
        if not w: return (None,None,k)
        i,j,d = w
        k += 1
        if input[i][j] != '.': break
    return (i+diri[d],j+dirj[d],k+1)

# Exploration:  make sure all of the above works
for i,j,d in V:
    for e in range(4):
        u,v = i+diri[d], j+dirj[d]
        if input[u+diri[e]][u+dirj[e]] == '.':
            u,v,k = find_next_junction(u,v,e)
            if u:
                print(f'From {i},{j} going {d}, {k} steps to {u},{v}')
            else:
                print(f'From {i},{j} going {d}, {k} steps to dead end')


# Compute distances between the junctions, while obeying
src = (0,1); dst = (n,m-2)
