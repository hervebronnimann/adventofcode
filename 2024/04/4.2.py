import itertools

grid = open("example.txt",'r').read().strip().split('\n')
print(grid)

def find_xmas(i,j):
    if i==0 and j==0: return 0
    n = 0
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid[x])-1):
            if [grid[x-i][y-j],grid[x+i][y-j],grid[x][y],grid[x-i][y+j],grid[x+i][y+j]]  == ['M','M','A','S','S']: n = n + 1
            if [grid[x-i][y-j],grid[x-i][y+j],grid[x][y],grid[x+i][y-j],grid[x+i][y+j]]  == ['M','M','A','S','S']: n = n + 1
    return n

print(sum([find_xmas(i,j) for (i,j) in itertools.product(*[[-1,1],[-1,1]])]) / 2)
