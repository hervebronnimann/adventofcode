# n1,n2,input=10,10,'.^^.^.^^^^'
n1,n2,input=40,400000,'^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^'

def istrap(x):
    if x[0]=='^' and x[2]=='.': return '^'
    if x[2]=='^' and x[0]=='.': return '^'
    return '.'

def nextrow(row):
    row = '.'+row+'.'
    return ''.join([istrap(row[i-1:i+2]) for i in range(1,len(row)-1)])

grid = []
for _ in range(n1):
    grid.append(input)
    input = nextrow(input)
print('Part 1:','\n'.join(grid).count('.'))

for _ in range(n1,n2):
    grid.append(input)
    input = nextrow(input)
print('Part 2:','\n'.join(grid).count('.'))
