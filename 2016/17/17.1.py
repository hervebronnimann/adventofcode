import hashlib
from collections import deque

dir = { 'R':0, 'D':1, 'L':2, 'U':3 }
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

def bfs(src,dst):
    pq = deque()
    pq.append((0,src,''))
    while pq:
        i,node,path = pq.popleft()
        for adjnode,d in adj(node,path):
            if adjnode == dst: return i+1,path+d
            if adjnode[0] < src[0] or adjnode[0] > dst[0]: continue
            if adjnode[1] < src[1] or adjnode[1] > dst[1]: continue
            pq.append((i+1, adjnode, path+d))
    return float('inf'),''

def md5salt(x):
    return hashlib.md5((input+str(x)).encode('utf-8')).hexdigest()

def adj(x,path):
    h = md5salt(path)
    for i,d in enumerate("UDLR"):
        if h[i] in 'bcdef': yield (x[0]+diri[dir[d]],x[1]+dirj[dir[d]]),d

# input = 'ihgpwlah'
# input = 'kglvqrro'
# input = 'ulqzkmiv'
input = 'vwbaicqe'
print(bfs((1,1),(4,4)))
