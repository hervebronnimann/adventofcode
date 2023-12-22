import re
from collections import defaultdict

input = open("example.txt",'r').read().strip().split('\n')

B = []; i = 0
for brick in input:
    x1,y1,z1,x2,y2,z2 = [ int(x) for x in re.sub('[,~]', ' ',brick).strip().split(' ')]
    s = chr(ord('A')+i)  # later, for input s = str(i)
    #s = str(i)
    if x1==x2 and y1==y2:
        B.append( ('Z',x1,y1,z1,z2-z1,s) )
    elif z1==z2 and y1==y2:
        B.append( ('X',x1,y1,z1,x2-x1,s) )
    elif x1==x2 and z1==z2:
        B.append( ('Y',x1,y1,z1,y2-y1,s) )
    i += 1
print([x for x in B if x[4]<0] or f"The {len(B)} bricks are ordered in x,y, and z")

# sort by increasing Z values
B.sort(key = lambda x: x[3])

# compute H map floor is at 0, and fall the blocks
# as well as a directed graph of support, A->B if A supports B
# as well as the reverse graph of support, B->A if B rests on A
BRICKS = [node[5] for node in B]
SUPP = { b:set() for b in BRICKS }
REST = { b:set() for b in BRICKS }
H = defaultdict(lambda: (0,None))
for i,(t,x,y,z,n,s) in enumerate(B):
    if t=='Z': h = 1 + H[(x,y)][0]
    elif t=='X': h = 1 + max([H[(u,y)][0] for u in range(x,x+n+1)])
    elif t=='Y': h = 1 + max([H[(x,u)][0] for u in range(y,y+n+1)])
    else:  printf("Unknown brick type")
    # print(f"Block {s} falls from {z} to {h}")
    B[i] = (t,x,y,h,n)
    if t=='Z':
        b = H[(x,y)][1]
        if b: SUPP[b].add(s); REST[s].add(b)
        H[(x,y)] = (h+n,s)
    if t=='X':
        for u in range(x,x+n+1):
            b = H[(u,y)][1]
            if b and H[(u,y)][0]==h-1: SUPP[b].add(s); REST[s].add(b)
            H[(u,y)] = (h,s)
    if t=='Y':
        for u in range(y,y+n+1):
            b = H[(x,u)][1]
            if b and H[(x,u)][0]==h-1: SUPP[b].add(s); REST[s].add(b)
            H[(x,u)] = (h,s)
# print(H)
print(SUPP)
print(REST)

res = 0
for i,b in enumerate(BRICKS):
    wouldFall = set([b])
    for b2 in BRICKS[i+1:]:
        if REST[b2].issubset(wouldFall):
            wouldFall.add(b2)
    res += len(wouldFall)-1
    if len(wouldFall)>1: print(f"Block {b} would fall {wouldFall}")
print(res)
