import itertools

grid = []
with open("input.txt",'r') as f:
  for s in f:
    grid.append(s.strip())

def find_xmas(i,j):
    if i==0 and j==0: return 0
    n = 0
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid[x])-1):
            if [grid[x-i][y-j],grid[x+i][y-j],grid[x][y],grid[x-i][y+j],grid[x+i][y+j]]  == ['M','M','A','S','S']: n = n + 1
            if [grid[x-i][y-j],grid[x-i][y+j],grid[x][y],grid[x+i][y-j],grid[x+i][y+j]]  == ['M','M','A','S','S']: n = n + 1
    return n

print(sum([find_xmas(i,j) for (i,j) in itertools.product(*[[-1,1],[-1,1]])]) / 2)
