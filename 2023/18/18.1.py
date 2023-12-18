input = open("input.txt",'r').read().strip().split('\n')

# 0,1,2,3 -> R,D,L,U
dir = { 'R':0, 'D':1, 'L':2, 'U':3 }
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

# Graph of (i,j)
i,j= (0,0)
g = set([(0,0)])
for x in input:
    d,n,_ = x.split(' '); n = int(n)
    while n > 0:
        n -= 1
        i += diri[dir[d]]
        j += dirj[dir[d]]
        g.add((i,j))
print(g)

mini = min([x for x,_ in g])
maxi = max([x for x,_ in g])
minj = min([x for _,x in g])
maxj = max([x for _,x in g])
print(mini,maxi,minj,maxj)

x = ""; outside = set(); q = []
for i in range(mini, maxi+1):
    if (i,minj) not in g: outside.add((i,minj)); q.append((i,minj))
    if (i,maxj) not in g: outside.add((i,maxj)); q.append((i,maxj))
for j in range(minj, maxj+1):
    if (mini,j) not in g: outside.add((mini,j)); q.append((mini,j))
    if (maxi,j) not in g: outside.add((maxi,j)); q.append((maxi,j))
while len(q) > 0:
    i,j = q.pop()
    if i>mini and (i-1,j) not in g and (i-1,j) not in outside: outside.add((i-1,j)); q.append((i-1,j))
    if i<maxi and (i+1,j) not in g and (i+1,j) not in outside: outside.add((i+1,j)); q.append((i+1,j))
    if j>minj and (i,j-1) not in g and (i,j-1) not in outside: outside.add((i,j-1)); q.append((i,j-1))
    if j<maxj and (i,j+1) not in g and (i,j+1) not in outside: outside.add((i,j+1)); q.append((i,j+1))
print((maxi+1-mini)*(maxj+1-minj) - len(outside))
