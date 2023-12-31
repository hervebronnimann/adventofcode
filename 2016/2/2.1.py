input = open("input.txt",'r').read().strip().split('\n')

dd = { 'R':0, 'D':1, 'L':2, 'U':3 }
di = [ 0, 1, 0, -1 ]
dj = [ 1, 0, -1, 0 ]

grid = [ '123', '456', '789' ]

def clamp(x,m,M):
    if x<m: return m
    if x>M: return M
    return x

def move(i,j,c):
    d = dd[c]
    return clamp(i+di[d],0,2), clamp(j+dj[d],0,2)

res = ''
i,j = 1,1
for row in input:
    for x in row:
        i,j = move(i,j,x)
    res += grid[i][j]
print(res)
