import re

rules = open("input.txt").read().strip().split('\n\n')
# rules = open("example.txt").read().strip().split('\n\n')

def det(a,b,c,d): return a*d - b*c

def solve(ax,ay,bx,by,px,py):
    d = det(ax,bx,ay,by)
    # print(f"Det: {d}")
    if d == 0: return 0
    a = det(px,bx,py,by)
    b = det(ax,px,ay,py)
    # print(f"A,B: {a},{b}")
    if a % d != 0 or b % d != 0: return 0
    if a*d < 0 or b*d < 0: return 0
    # print(f"Sol: {(a//d)*3} + {(b//d)}")
    return (a//d)*3 +(b//d)

n = 0
for r in rules:
    a,b,p = r.split('\n')
    A = re.search(r'Button A: X\+(\d+), Y\+(\d+)', a)
    ax,ay = int(A.group(1)), int(A.group(2))
    B = re.search(r'Button B: X\+(\d+), Y\+(\d+)', b)
    bx,by = int(B.group(1)), int(B.group(2))
    P = re.search(r'Prize: X=(\d+), Y=(\d+)', p)
    px,py = int(P.group(1)), int(P.group(2))
    n += solve(ax,ay,bx,by,px,py)
print(n)
