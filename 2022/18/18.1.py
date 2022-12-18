def parse(l): x,y,z=l.split(','); return (1+int(x),1+int(y),1+int(z))
lines = list(map(parse, open("input.txt").read().strip().split('\n')))
print(list(lines))

X=max([x+1 for x,_,_ in lines])
Y=max([y+1 for _,y,_ in lines])
Z=max([z+1 for _,_,z in lines])
print((X,Y,Z))

dX = [set([(y,z) for _,y,z in filter(lambda t: t[0]==x0, lines)]) for x0 in range(X+1)]
dY = [set([(x,z) for x,_,z in filter(lambda t: t[1]==y0, lines)]) for y0 in range(Y+1)]
dZ = [set([(x,y) for x,y,_ in filter(lambda t: t[2]==z0, lines)]) for z0 in range(Z+1)]

ans = 0
for x in range(1,X+1): ans += len(dX[x].symmetric_difference(dX[x-1]))
for y in range(1,Y+1): ans += len(dY[y].symmetric_difference(dY[y-1]))
for z in range(1,Z+1): ans += len(dZ[z].symmetric_difference(dZ[z-1]))
print(ans)
