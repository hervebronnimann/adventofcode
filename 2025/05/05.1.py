sol = 0
ranges = []
for l in open('input.txt','r'):
    l = l.strip()
    if '-' in l:
        x,y = l.split('-')
        ranges.append( (int(x),int(y)) )
    elif len(l) == 0:
        print(ranges)
    else:
        z = int(l)
        if any(x <= z and z <= y for (x,y) in ranges):
            print(f'{z} is fresh')
            sol += 1
print(sol)
