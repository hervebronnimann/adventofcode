import re

input = open("input.txt",'r').read().strip().split('\n')
n = 6; m = 50

grid = [ ['.']*m for _ in range(n) ]

def rect(n,m):
    for i in range(n):
        for j in range(m):
            grid[i][j] = '#'

def rotrow(i,n):
    grid[i] = grid[i][m-n:] + grid[i][0:m-n]

def rotcol(j,m):
    col = [ grid[i][j] for i in range(n) ]
    col = col[n-m:] + col[0:n-m]
    for i in range(n): grid[i][j] = col[i]

for row in input:
    row = re.sub(' by ', ' ', row)
    row = re.sub(' [xy]=', ' ', row)
    row = re.sub('rotate ', '', row)
    row = re.sub('x', ' ', row)
    cmd,x,y = row.split()
    x = int(x); y = int(y)
    if cmd=='rect': rect(y,x)
    elif cmd=='row': rotrow(x,y)
    elif cmd=='column': rotcol(x,y)

pict = '\n'.join([''.join(row) for row in grid])
print("Part 1:", pict.count('#'))

print("Part 2:")
print(pict)
