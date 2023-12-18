input = open("input.txt",'r').read().strip().split('\n')

# 0,1,2,3 -> R,D,L,U
dir = { 'R':0, 'D':1, 'L':2, 'U':3 }
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

# Polygon, points on the boundary
i,j= (0,0)
p = [(i,j)]; boundary = 0
for x in input:
    _,_,h = x.split(' ')
    d = int(h[-2])
    n = int(h[2:-2],16)
    boundary += n
    i += n*diri[d]
    j += n*dirj[d]
    p.append((i,j))

area = 0
for i in range(len(p)):
    x1,y1 = p[i]
    x2,y2 = p[(i+1) % len(p)]
    area += x2 * y1 - x1 * y2

# Pick's theorem:  area = inside + boundary / 2 - 1
inside = (area - boundary)//2 + 1
print( L + inside )
