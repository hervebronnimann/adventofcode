import re
import math
import functools

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

# OTOH if you work it out a little longer:
#   (vx-vx1)(y-y1)=(vy-vy1)(x-x1)
#   (vx-vx2)(y-y2)=(vy-vy2)(x-x2)
#   (vx-vx3)(y-y3)=(vy-vy3)(x-x3)
#   (vx-vx4)(y-y4)=(vy-vy4)(x-x4)
#   (vx-vx5)(y-y5)=(vy-vy5)(x-x5)
# You see that the x*vy and y*vx terms can be eliminated by subtracting any two equations.
# This leaves (2-1, 3-1, 4-1, and 5-1):
#   vx2*(y-y2)-vx1*(y-y1)+vx*(y2-y1) = vy2*(x-x2)-vy1*(x-x1)+vy*(x2-x1)
#   vx3*(y-y3)-vx1*(y-y1)+vx*(y3-y1) = vy3*(x-x3)-vy1*(x-x1)+vy*(x3-x1)
#   vx4*(y-y4)-vx1*(y-y1)+vx*(y4-y1) = vy4*(x-x4)-vy1*(x-x1)+vy*(x4-x1)
#   vx5*(y-y5)-vx1*(y-y1)+vx*(y5-y1) = vy5*(x-x5)-vy1*(x-x1)+vy*(x5-x1)
# Now we have 4 equations and four unknowns, x, y, vx, and vy.  We can solve.
#   [ vy1-vy2  vx2-vx1  y2-y1  x2-x1 ]   [ x  ]   [ vx2*y2-vy2*x2+vy1*x1-vx1*y1 ]
#   [ vy1-vy3  vx3-vx1  y3-y1  x3-x1 ] * [ y  ] = [ vx3*y3-vy3*x3+vy1*x1-vx1*y1 ]
#   [ vy1-vy4  vx4-vx1  y4-y1  x4-x1 ]   [ vx ]   [ vx4*y4-vy4*x4+vy1*x1-vx1*y1 ]
#   [ vy1-vy5  vx5-vx1  y5-y1  x5-x1 ]   [ vy ]   [ vx5*y5-vy5*x5+vy1*x1-vx1*y1 ]
# Once solved, also solve with first two lines, for x and vx, and then check.
#   vx2*(z-z2)-vx1*(z-z1)+vx*(y2-y1) = vy2*(x-x2)-vy1*(x-x1)+vy*(x2-x1)
#   vx3*(z-z3)-vx1*(z-z1)+vx*(y3-y1) = vy3*(x-x3)-vy1*(x-x1)+vy*(x3-x1)
#   vx4*(z-z4)-vx1*(z-z1)+vx*(y4-y1) = vy4*(x-x4)-vy1*(x-x1)+vy*(x4-x1)

def check(x,y,z,vx,vy,vz):
    # T = []
    for ux,uy,uz,wx,wy,wz in input:
        tx = (x-ux)/(wx-vx) if wx-vx!=0 else math.inf
        ty = (y-uy)/(wy-vy) if wy-vy!=0 else math.inf
        tz = (z-uz)/(wz-vz) if wz-vz!=0 else math.inf
        print(ux,uy,uz,wx,wy,wz,tx,ty,tz)
        if tx<0 or ty<0 or tz<0: return False
        if (x-ux)*(wy-vy)!=(y-uy)*(wx-vx): return False  # tx!=ty
        if (x-ux)*(wz-vz)!=(z-uz)*(wx-vx): return False # tx!=tz
        # T.append(tx)
    print(f'Solution: {x+y+z} for {x},{y},{z} with velocity {vx},{vy},{vz}') # ,T)
    exit(1)

x1,y1,z1,vx1,vy1,vz1 = input[0]
x2,y2,z2,vx2,vy2,vz2 = input[1]
x3,y3,z3,vx3,vy3,vz3 = input[2]
x4,y4,z4,vx4,vy4,vz4 = input[3]
x5,y5,z5,vx5,vy5,vz5 = input[4]

def simplify(A,b):
    d = functools.reduce(math.gcd,(A[0] or 1,A[1] or 1,A[2] or 1,A[3] or 1,b or 1))
    A[0] //= d; A[1] //= d; A[2] //= d; A[3] //= d; b //= d
    return b

# Gaussian elimination, with gcd
def gaussian(A,B):
    for n in range(0,4):
        B[n] = simplify(A[n],B[n])
        for i in range(n+1,4):
            for j in range(n+1,4):
                A[i][j] = A[i][j] * A[n][n] - A[i][n] * A[n][j]
            B[i] = B[i] * A[n][n] - B[n] * A[i][n]
            A[i][n] = 0
            B[i] = simplify(A[i],B[i])
    vy = B[3] / A[3][3]
    vx = (B[2] - vy * A[2][3]) / A[2][2]
    y  = (B[1] - vy * A[1][3] - vx * A[1][2]) / A[1][1]
    x  = (B[0] - vy * A[0][3] - vx * A[0][2] - y * A[0][1]) / A[0][0]
    return (x,y,vx,vy)

# Do it on x,y
A1 = [ vy1-vy2, vx2-vx1, y2-y1, x2-x1 ]; b1 = vx2*y2-vy2*x2+vy1*x1-vx1*y1
A2 = [ vy1-vy3, vx3-vx1, y3-y1, x3-x1 ]; b2 = vx3*y3-vy3*x3+vy1*x1-vx1*y1
A3 = [ vy1-vy4, vx4-vx1, y4-y1, x4-x1 ]; b3 = vx4*y4-vy4*x4+vy1*x1-vx1*y1
A4 = [ vy1-vy5, vx5-vx1, y5-y1, x5-x1 ]; b4 = vx5*y5-vy5*x5+vy1*x1-vx1*y1

x,y,vx,vy = gaussian([A1, A2, A3, A4], [ b1, b2, b3, b4 ])

# Do it on x,z
A1 = [ vz1-vz2, vx2-vx1, z2-z1, x2-x1 ]; b1 = vx2*z2-vz2*x2+vz1*x1-vx1*z1
A2 = [ vz1-vz3, vx3-vx1, z3-z1, x3-x1 ]; b2 = vx3*z3-vz3*x3+vz1*x1-vx1*z1
A3 = [ vz1-vz4, vx4-vx1, z4-z1, x4-x1 ]; b3 = vx4*z4-vz4*x4+vz1*x1-vx1*z1
A4 = [ vz1-vz5, vx5-vx1, z5-z1, x5-x1 ]; b4 = vx5*z5-vz5*x5+vz1*x1-vx1*z1

_,z,_,vz = gaussian([A1, A2, A3, A4], [ b1, b2, b3, b4 ])

x = round(x); y = round(y); z = round(z)
print(check(x,y,z,vx,vy,vz))
print(x+y+z)
