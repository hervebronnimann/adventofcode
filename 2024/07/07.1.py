lines = [ x.split(': ') for x in open("input.txt",'r').read().strip().split('\n') ]

def solve(r, x, y):
    if len(y) == 0: return r == x
    if solve(r, x + y[0], y[1:]): return True
    if solve(r, x * y[0], y[1:]): return True
    return False

n = 0
for l in lines:
    r = int(l[0])
    x = [ int(x) for x in l[1].split() ]
    if solve(r,0,x): n += r
print(n)
