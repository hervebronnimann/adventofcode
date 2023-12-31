input = open("input.txt",'r').read().strip().split('\n')

dd = { 'R':0, 'D':1, 'L':2, 'U':3 }
di = [ 0, 1, 0, -1 ]
dj = [ 1, 0, -1, 0 ]

grid = [ '  1  ', ' 234 ', '56789', ' ABC ', '  D  ' ]

def clamp(x,m,M):
    if x<m: return m
    if x>M: return M
    return x

def move(i,j,c):
    d = dd[c]
    u,v = clamp(i+di[d],0,4), clamp(j+dj[d],0,4)
    if grid[u][v]==' ': return i,j
    return u,v

res = ''
i,j = 0,2
for row in input:
    for x in row:
        i,j = move(i,j,x)
    res += grid[i][j]
print(res)
