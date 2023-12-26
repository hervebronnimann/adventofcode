from collections import deque

input = open("example.txt",'r').read().strip().split('\n')
input = [ list(row) for row in input ]
n = len(input); m = len(input[0])

# 0,1,2,3 -> R,D,L,U
dir = { 'R':0, 'D':1, 'L':2, 'U':3 }
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
V = [ (0,1), (n-1,m-2) ]
for i in range(n):
    for j in range(m):
        if input[i][j] != '.': continue
        if sum([1 if input[x][y] in '><v^' else 0 for x,y in neighbors(i,j)]) > 1:
            input[i][j]=chr(ord('A')+len(V)-2)
            V.append((i,j))
        elif sum([1 if input[x][y]=='.><v^' else 0 for x,y in neighbors(i,j)]) > 2:
            print(f'Vertex {i},{j} a junction without clear ><v^ markers')
print(V)
print("\n".join([ "".join(x) for x in input]))

# Compute distances between the junctions, while obeying
D = { v:0 for v in V }
Q = deque(V); visited = set(V)
# while len(Q)>0:

