c = list(open("input.txt",'r').read().strip())  # c for compact

id = 0
u = []  # u for uncompressed
for i in range(len(c)//2):
    u = u + ([id] * int(c[2*i]))
    u = u + (['.'] * int(c[2*i+1]))
    id += 1
if len(c) %2 == 1:
    u = u + ([id] * int(c[-1]))
print(u)

p = len(u)-1  # p for position
for i in range(len(u)):
    if u[i]=='.':
        while i < p and u[p]=='.': p -= 1
        if p <= i: break
        u[i],u[p] = u[p],u[i]

print(sum([ i * u[i] for i in range(len(u)) if u[i] != '.']))
