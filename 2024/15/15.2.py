rules = open("input.txt").read().strip().split('\n\n')
# rules = open("example.txt").read().strip().split('\n\n')

xx = { 'O':'[]', '#':'##', '.':'..', '@': '@.' }
grid = [ list(''.join([ xx[c] for c in x])) for x in rules[0].split('\n') ]
n = len(grid)
m = len(grid[0])
# print('\n'.join([''.join(l) for l in grid]))

moves = rules[1].replace('\n','')
# print(moves)

def find_org():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                grid[i][j]='.'
                return i,j

def movey(x,y,dy):
    if grid[x][y+dy] == '#':
        return False
    if grid[x][y+dy] == '.' or movey(x,y+dy,dy):
        grid[x][y+dy] = grid[x][y]
        grid[x][y] = '.'
        return True
    return False

def closure(x,Y,dx):
    if len(Y) == 0: return []
    result = [(x,y) for y in Y]
    Z = set()
    for y in Y:
        if grid[x+dx][y] == '[':
            Z.add(y)
            Z.add(y+1)
        if grid[x+dx][y] == ']':
            Z.add(y-1)
            Z.add(y)
    return closure(x+dx,Z,dx) + result

def movex(x,y,dx):
    C = closure(x,[y],dx)
    for i,j in C:
        if grid[i+dx][j] == '#':
            return False
    for i,j in C:
        grid[i+dx][j] = grid[i][j]
        grid[i][j] = '.'
    return True

dx = { '<': 0, '>': 0, '^': -1, 'v': 1 }
dy = { '<': -1, '>': 1, '^': 0, 'v': 0 }
x,y = find_org()
for p in moves:
    if dx[p]==0 and movey(x,y,dy[p]):
        y += dy[p]
    if dx[p]!=0 and movex(x,y,dx[p]):
        x += dx[p]
    grid[x][y] = '@'
# print('\n'.join([''.join(l) for l in grid]))
# grid[x][y] = '.'
# print(x,y)

def gps(grid):
    g = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '[':
                g += 100 * i + j
    return g

print(gps(grid))
