c = list(open("input.txt",'r').read().strip())

id = 0
u = []
for i in range(len(c)//2):
    u = u + ([(id,int(c[2*i]))] * int(c[2*i]))
    u = u + [('.',k) for k in range(int(c[2*i+1]),0,-1)]
    id += 1
if len(c) %2 == 1:
    u = u + ([(id,int(c[-1]))] * int(c[-1]))
print(u)

p = len(u)-1
for i in range(len(u)-1,0,-1):
    if u[i][0]=='.': continue
    for j in range(i):
        if u[j][0]!='.' or u[j][1] < u[i][1]: continue
        for k in range(u[i][1]):
            u[j+k],u[i-k] = u[i-k],u[j+k]
        break
print(u)

print(sum([ i * u[i][0] for i in range(len(u)) if u[i][0] != '.']))
