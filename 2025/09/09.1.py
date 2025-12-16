def area(p,q): return (1+abs(p[0]-q[0])) * (1+abs(p[1]-q[1]))

points = []
for l in open('input.txt','r'):
    x,y = [int(x) for x in l.split(',')]
    points.append((x,y))
n = len(points)

a = 0
for i in range(n):
    for j in range(i+1,n):
        a = max(a,area(points[i],points[j]))
print(a)
