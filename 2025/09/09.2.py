def area(p,q): return (1+abs(p[0]-q[0])) * (1+abs(p[1]-q[1]))

points = []
for l in open('input.txt','r'):
    x,y = [int(x) for x in l.split(',')]
    points.append((x,y))
n = len(points)
points.append(points[0])

# Only those points matter
XX = sorted(set([x for x,_ in points]))
YY = sorted(set([y for _,y in points]))

X = set()
for i in range(len(XX)-1):
    if XX[i] < XX[i+1]:
        X.add((XX[i]+XX[i+1])/2)
X = sorted(X)
print(X)

Y = set()
for j in range(len(YY)-1):
    if YY[j] < YY[j+1]:
        Y.add((YY[j]+YY[j+1])/2)
Y = sorted(Y)
print(Y)

def between(x,y,z):
    return (y < x and x < z) if y < z else (z < x and x < y)

def det(p,q,r):
    return (q[0]-p[0]) * (r[1]-p[1]) - (r[0]-p[0]) * (q[1]-p[1])

def inside(p,points):
    res = 0
    for i in range(len(points)-1):
        if points[i][0] == points[i+1][0] and p[0] < points[i][0]:
            if between(p[1],points[i][1],points[i+1][1]):
                res += 1
    return res%2 != 0

P = set()
for x in X:
    for y in Y:
        if inside((x,y),points):
           P.add((x,y))

def subrange(X,x0,x1):
    if x0 > x1: x0,x1=x1,x0
    for x in X:
        if x < x0: continue
        if x <= x1: yield x

a = 0
for i in range(n):
    for j in range(n):
        good = True
        for x in subrange(X,points[i][0],points[j][0]):
            for y in subrange(Y,points[i][1],points[j][1]):
                if (x,y) not in P:
                    good = False; break
        if good:
            a = max(a,area(points[i],points[j]))
print(a)
