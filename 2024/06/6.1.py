grid = [ list(x) for x in open("input.txt",'r').read().strip().split('\n') ]

x,y = -1,-1
for u in range(len(grid)):
    if '^' in grid[u]:
        x,y = u,''.join(grid[u]).find('^')
print(grid,x,y)

def advance(dx,dy):
    global x,y
    while (0 <= x and x < len(grid) and 0 <= y and y < len(grid[x])):
        grid[x][y] = 'X'
        if (0 <= x+dx and x+dx < len(grid) and 0 <= y+dy and y+dy < len(grid[x])) and grid[x+dx][y+dy] == '#':
            return True
        x += dx
        y += dy
    return False

dx,dy = -1,0
while advance(dx,dy): dx,dy = dy,-dx
#print('\n'.join([ ''.join(x) for x in grid]))
print(sum([ line.count('X') for line in grid]))
