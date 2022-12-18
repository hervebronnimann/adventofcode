def parse(l): x,y,z=l.split(','); return (1+int(x),1+int(y),1+int(z))
lines = list(map(parse, open("input.txt").read().strip().split('\n')))
X = [max([t[k]+1 for t in lines]) for k in range(3)]
dX = [[set([tuple(t[:k]+t[k+1:]) for t in filter(lambda t: t[k]==x, lines)]) for x in range(X[k]+1)] for k in range(3)]
ans = sum([sum([len(dX[k][x].symmetric_difference(dX[k][x-1])) for x in range(1,X[k]+1)]) for k in range(3)])
print(ans)
