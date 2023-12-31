input = open("input.txt",'r').read().strip().split(', ')

di = [ 0, 1, 0, -1 ]
dj = [ 1, 0, -1, 0 ]

def explore():
    i,j,d = 0,0,3
    visit = set((i,j))
    for step in input:
        d = (d+1 if step[0]=='R' else d+3) % 4
        s = int(step[1:])
        for t in range(1,s+1):
           i,j = i+di[d], j+dj[d]
           if (i,j) in visit: return (i,j)
           visit.add((i,j))

i,j = explore()
print(i,j, i+j)
