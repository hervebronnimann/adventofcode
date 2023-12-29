import re
input = open("input.txt",'r').read().strip().split('\n')
input = [ [ int(x) for x in re.sub('[,@ ]+', ' ', row).split(' ') ] for row in input ]
n = len(input)
print(n,input[0])

m = 7
M = 27
m = 200000000000000
M = 400000000000000

def check(a, b):
    x1,y1,_,vx1,vy1,_ = a
    x2,y2,_,vx2,vy2,_ = b
    # solve for x1 + t1*vx1 == x2 + t2*vx2 and y1 + t1*vy1 == y2 + t2*vy2
    #  t2*vx2 - t1*vx1 + (x2-x1) == 0   (* vy1 to eliminate t1)  (* vy2)
    #  t2*vy2 - t1*vy1 + (y2-y1) == 0   (* vx1 to eliminate t1)  (* vx2)
    det = vx2 * vy1 - vy2 * vx1
    if det == 0: return False
    t2 = ( -(x2-x1)*vy1 + (y2-y1)*vx1 ) / det
    t1 = ( -(x2-x1)*vy2 + (y2-y1)*vx2 ) / det
    # if t1 < 0: print(f'Rows {a},{b} cross at t1={t1}<0')
    # if t2 < 0: print(f'Rows {a},{b} cross at t2={t2}<0')
    if t1 < 0 or t2 < 0: return False
    x,y = x2 + t2*vx2, y2 + t2*vy2
    # print(f'Rows {a},{b} will cross at ({x},{y})')
    if x < m or x > M : return False
    if y < m or y > M : return False
    return True

res = 0
for i in range(n):
    for j in range(i+1,n):
        if check(input[i],input[j]): res += 1
print(res)
