import itertools

grid = []
with open("example.txt",'r') as f:
  for s in f:
    grid.append(s.strip())

def find_xmas(i,j):
    if i==0 and j==0: return 0
    n = 0
    for x in range(0,len(grid)):
        if x+3*i not in range(0,len(grid)): continue
        for y in range(0,len(grid[0])):
            if y+3*j not in range(0,len(grid[0])): continue
            if [grid[x+i*k][y+j*k] for k in range(0,4)] == ['X','M','A','S']: n = n + 1
    return n

print(sum([find_xmas(i,j) for (i,j) in itertools.product(*[[-1,0,1],[-1,0,1]])]))
