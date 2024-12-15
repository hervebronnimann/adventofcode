import re

rules = open("input.txt").read().strip().split('\n\n')
# rules = open("example.txt").read().strip().split('\n\n')

grid = [ list(x) for x in rules[0].split('\n') ]
n = len(grid)
m = len(grid[0])

moves = rules[1].replace('\n','')
# print(moves)

def find_org():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                grid[i][j]=','
                return i,j

def move(x,y,dx,dy):
    if grid[x+dx][y+dy] == '#':
        return False
    if grid[x+dx][y+dy] == '.' or move(x+dx,y+dy,dx,dy):
        grid[x+dx][y+dy] = grid[x][y]
        grid[x][y] = '.'
        return True
    return False

dx = { '<': 0, '>': 0, '^': -1, 'v': 1 }
dy = { '<': -1, '>': 1, '^': 0, 'v': 0 }
x,y = find_org()
for p in moves:
    if move(x,y,dx[p],dy[p]):
        x += dx[p]
        y += dy[p]
print('\n'.join([''.join(l) for l in grid]))

def gps(grid):
    g = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                g += 100 * i + j
    return g

print(gps(grid))
