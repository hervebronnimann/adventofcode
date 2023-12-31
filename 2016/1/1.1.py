input = open("input.txt",'r').read().strip().split(', ')

di = [ 0, 1, 0, -1 ]
dj = [ 1, 0, -1, 0 ]

i,j,d = 0,0,3
for step in input:
    d = (d+1 if step[0]=='R' else d+3) % 4
    s = int(step[1:])
    i,j = i+s*di[d], j+s*dj[d]
print(i,j, i+j)
