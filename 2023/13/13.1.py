from functools import cache

input = open("example.txt",'r').read().strip().split('\n\n')
input = open("input.txt",'r').read().strip().split('\n\n')

def solve(y:list):
    for i in range(len(y)-1):
        found = True
        # 0..i i+1..min(2*i,len(y)) if 
        for j in range(min(i+1,len(y)-1-i)):
            if y[i-j] != y[i+j+1]:
                found = False; break
        if found: return i+1
    return 0

def transpose(y:list):
  return ["".join(x) for x in zip(*y)]

res = 0
for x in input:
    y = x.split('\n')
    v = solve(y)
    h = solve(transpose(y))
    res += h + 100*v
print(res)
