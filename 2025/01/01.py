sol = 0
x = 50

for line in open('input.txt','r'):
    if line[0] == 'L':
        x -= int(line[1:])
    elif line[0] == 'R':
        x += int(line[1:])
    if x % 100 ==0: sol += 1

print(sol)
