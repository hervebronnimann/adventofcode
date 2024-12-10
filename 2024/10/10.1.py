from collections import defaultdict

grid = [ list(x) for x in open("input.txt",'r').read().strip().split('\n') ]
# grid = [ list(x) for x in open("example.txt",'r').read().strip().split('\n') ]

n = len(grid)
m = len(grid[0])
def valid(i,j): return i in range(n) and j in range(m)

digits = defaultdict(list)
for i,l in enumerate(grid):
        for j,x in enumerate(l):
            digits[int(grid[i][j])].append((i,j))
# print(digits)

trails = [ [t] for t in digits[0] ]
# print(trails)

for k in range(1,10):
    trails2 = []
    for t in trails:
        i,j = t[-1]
        for u,v in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
            if valid(u,v) and int(grid[u][v]) == k:
                trails2.append(t+[(u,v)])
    trails = trails2
    # print(trails)

r = 0
for i,j in digits[0]:
    score = len(set([ t[9] for t in trails if t[0]==(i,j)]))
    # print(f"({i},{j}) has score {score}")
    r += score
print(r)

