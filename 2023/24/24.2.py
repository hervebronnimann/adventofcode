import re
import math

input = open("input.txt",'r').read().strip().split('\n')
input = [ [ int(x) for x in re.sub('[,@ ]+', ' ', row).split(' ') ] for row in input ]
n = len(input)

# Our rock travels as p+t*v.  And so p+t*v == pi+t*vi for every i must have a
# solution in t.  The problem statement (on the example) implies that these
# solutions in t are also integral, but this is not a hard requirement, and
# it's quite possible that they are not for the given input.  There is also no
# requirement that the input gives the hailstones in the order they are hit by
# the rock, and indeed this is not the case for the example.  Finally, the
# solutions in t must all be >0.

# Let's write down for x1 only:
#   x+t*vx = x1+t*vx1    y+t*vy = y1+t*yx1    z+t*vz = z1+t*vz1
# Let's eliminate the variable t:
#   x1-x=t(vx-vx1) =>   -1/t=(vx-vx1)/(x-x1)=(vy-vy1)/(y-y1)=(vz-vz1)/(z-z1)
#   (vx-vx1)(y-y1)=(vy-vy1)(x-x1)
#   (vz-vz1)(y-y1)=(vy-vy1)(z-z1)
#   (vx-vx1)(z-z1)=(vz-vz1)(x-x1)
# This is quadratic and I'm not about to write a quadratic solver...


# I think the solution comes from having a range for vx,vy,vz, and exhaustively
# solving for x,y,z.  1000 * 1000 * 1000 Gives only a billion velocities to check.
# Alternately, we can do an incremental search on max(vx,vy,vz),and that will
# check the same space

# Assuming we know the velocity vx,vy,vz, and writing for the first two hailstones:
# [Notation: vxx1 = vx-vx1, etc.; vxx = lcm(vxx1,vxx2), dvxx=gcd(vxx1,vxx2), etc.]
#   vxx1(y-y1)=vyy1(x-x1)  =>  vxx*y = vyy1*vxx2/dvxx (x-x1) and vyy*x = vxx1/dvxx*vyy1 (y-y1)
#   vxx2(y-y2)=vyy2(x-x2)      vxx*y = vyy2*vxx1/dvxx (x-x2)     vyy*x = vxx1/dvxx*vyy1 (y-y1)
#   vxx1(z-z1)=vzz1(x-x1)      vxx1*z = vxx1*z1+vzz1*(x-x1)
# We can solve for x and see if it is an integer, and then solve for y and see if integer too.
# Finally, if we have a solution, we can solve for z and check for integer too.

def check(x,y,z,vx,vy,vz):
    # T = []
    for ux,uy,uz,wx,wy,wz in input:
        tx = (x-ux)/(wx-vx) if wx-vx!=0 else math.inf
        ty = (y-uy)/(wy-vy) if wy-vy!=0 else math.inf
        tz = (z-uz)/(wz-vz) if wz-vz!=0 else math.inf
        # print(ux,uy,uz,wx,wy,wz,tx,ty,tz)
        if tx<0 or ty<0 or tz<0: return False
        if (x-ux)*(wy-vy)!=(y-uy)*(wx-vx): return False  # tx!=ty
        if (x-ux)*(wz-vz)!=(z-uz)*(wx-vx): return False # tx!=tz
        # T.append(tx)
    print(f'Solution: {x+y+z} for {x},{y},{z} with velocity {vx},{vy},{vz}') # ,T)
    exit(1)
    return True

def solve(vx,vy,vz,h1,h2):
    x1,y1,z1,vx1,vy1,vz1 = h1[0],h1[1],h1[2],h1[3]-vx,h1[4]-vy,h1[5]-vz
    x2,y2,z2,vx2,vy2,vz2 = h2[0],h2[1],h2[2],h2[3]-vx,h2[4]-vy,h2[5]-vz
    # Rotate the coordinates as necessary, to ensure solvability
    rot = 0
    while rot < 3:
        if vx1*vx2 != 0 and vx1 * vy2 != vx2 * vy1: break
        x1,y1,z1,vx1,vy1,vz1 = y1,z1,x1,vy1,vz1,vx1
        x2,y2,z2,vx1,vy1,vz1 = y2,z2,x2,vy1,vz1,vx1
        rot += 1
    # If rotated three time, no solution (either identical, or parallel)
    if rot == 3: return False
    # Solve
    #   vx1(y-y1)=vy1(x-x1)  =>  vy1 * x - vx1 * y = vy1 * x1 - vx1 * y1 = w1
    #   vx2(y-y2)=vy2(x-x2)      vy2 * x - vx2 * y = vy2 * x2 - vx2 * y2 = w2
    w1 =  vy1 * x1 - vx1 * y1
    w2 =  vy2 * x2 - vx2 * y2
    det = -vy1*vx2 + vy2*vx1
    dx1 = -w1*vx2 + w2*vx1
    if dx1%det != 0: return False
    x = dx1//det
    dy1 = vy1*w2 - vy2*w1
    if dy1%vx1!= 0: return False
    y = dy1//det
    if vx1:
        # Solve vx1(z-z1)=vz1(x-x1)
        dz1 = vx1*z1+vz1*(x-x1)
        if dz1%vx1 != 0: return False
        z = dz1 // vx1
        x,y,z = (x,y,z) if rot==0 else (z,x,y) if rot==1 else (y,z,x)
        # print(f'A Possible {x},{y},{z} with rotation {rot}')
        return check(x,y,z,vx,vy,vz)
    elif vy1:
        dz1 = vy1*z1-vz1*(y-y1)
        if dz1%vy1 != 0: return False
        z = dz1 // vy1
        x,y,z = (x,y,z) if rot==0 else (z,x,y) if rot==1 else (y,z,x)
        # print(f'B Possible {x},{y},{z} with rotation {rot}')
        return check(x,y,z,vx,vy,vz)
    else:
        if vz1: print("Unhandled")
        # Else it's possible that v=v1 but in that case x=x1 and hailstone 1 is same as rock,
        # we should check that separately.  But if not, then v is not a solution.
        return False

# print(check(24, 13, 10, -3, 1, 2))

h1 = input[2]
h2 = input[3]

for n in range(1,2000):
    if n%10==0: print(n)
    for v1 in range(-n,n+1):
        for v2 in range(-n,n+1):
            solve(v1,v2,n,h1,h2)
            solve(v1,n,v2,h1,h2)
            solve(n,v1,v2,h1,h2)
            solve(v1,v2,-n,h1,h2)
            solve(v1,-n,v2,h1,h2)
            solve(-n,v1,v2,h1,h2)

