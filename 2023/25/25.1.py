from copy import deepcopy
from random import randrange

input = open("input.txt",'r').read().strip().split('\n')

nodes = set()
edges = []
for row in input:
    x,lst = row.split(': ')
    if len(x)!=3: print(x)
    for y in lst.split(' '):
        if len(y)!=3: print(y)
        nodes.add(x)
        nodes.add(y)
        edges.append((x,y))

def contract(u,v,nodes,edges):
    uv = u+v
    nodes.remove(u)
    nodes.remove(v)
    nodes.add(uv)
    new_edges = []
    for s,t in edges:
        if s==u or s==v:
            if t!=u and t!=v: new_edges.append((uv,t))
        elif t==u or t==v:
            if s!=u and s!=v: new_edges.append((s,uv))
        else:
            new_edges.append((s,t))
    return nodes,new_edges

def karger(N,E):
    nodes = deepcopy(N)
    edges = deepcopy(E)
    while len(nodes)>2:
        x = randrange(len(edges))
        u,v = edges[x]
        nodes,edges = contract(u,v,nodes,edges)
    return nodes

def degree(N0,N1,edges):
    res = 0
    for s,t in edges:
        if s in N0 and t in N1: res += 1
        if s in N1 and t in N0: res += 1
    return res

D = []
for i in range(10000):
    N = list(karger(nodes,edges))
    N0 = [ N[0][n:n+3] for n in range(0,len(N[0]),3) ]
    N1 = [ N[1][n:n+3] for n in range(0,len(N[1]),3) ]
    d = degree(N0,N1,edges)
    # print(d, N)
    D.append(d)
    if d == 3: print(len(N0)*len(N1),N0,N1); exit(1)
    elif i%10==0: print(D); D = []
