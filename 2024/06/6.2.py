grid = [ list(x) for x in open("input.txt",'r').read().strip().split('\n') ]

def find_start():
    for u in range(len(grid)):
        if '^' in grid[u]:
            return u,''.join(grid[u]).find('^')
x0,y0 = find_start()

#ugh use globals...
x,y,dx,dy = x0,y0,-1,0
def advance():
    global x,y,dx,dy
    while (0 <= x and x < len(grid) and 0 <= y and y < len(grid[x])):
        grid[x][y] = 'X'
        if (0 <= x+dx and x+dx < len(grid) and 0 <= y+dy and y+dy < len(grid[x])) and grid[x+dx][y+dy] == '#':
            return True
        x += dx
        y += dy
    return False

#part 1
while advance(): dx,dy = dy,-dx
print(sum([ line.count('X') for line in grid]))

#part 2
def loop():
    global x,y,dx,dy
    x,y,dx,dy = x0,y0,-1,0
    s = set()
    while advance() and (x,y,dx,dy) not in s:
        s.add((x,y,dx,dy))
        dx,dy = dy,-dx
    return 1 if (x,y,dx,dy) in s else 0

n = 0
for u in range(len(grid)):
    for v in range(len(grid[u])):
        if (u,v)==(x0,y0) or grid[u][v] == '#': continue
        grid[u][v] = '#'
        if loop(): n += 1
        grid[u][v] = '.'
        #print('\n'.join([ ''.join(x) for x in grid]))
print(n)
