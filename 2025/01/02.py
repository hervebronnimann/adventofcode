import math

sol = 0
x = 50

# for line in open('example.txt','r'):
for line in open('input.txt','r'):
    x0 = x
    if line[0] == 'L':
        x -= int(line[1:])
    elif line[0] == 'R':
        x += int(line[1:])
    # Now the number of multiples of 100 between (x0,x] depends on the ordering.
    # If x0<x, then (x//100)-(x0//100) but if x<x0, then essentially (-1) is inverting the inclusion/exclusion.
    count_up_to_x0 = math.floor(x0 / 100) if x0 < x else math.floor((x0-1)/100)
    count_up_to_x = math.floor(x / 100) if x0 < x else math.floor((x-1)/100)
    solinc = abs(count_up_to_x - count_up_to_x0)
    sol += solinc
    print(f"{line.strip()} x0={x0} x={x} sol += {solinc}")

print(sol)
