from functools import cache

input = open("example.txt",'r').read().strip().split('\n\n')
input = open("input.txt",'r').read().strip().split('\n\n')

def diff(x:str, y:str):
    if len(x) != len(y): return x + y
    return [(i,j) for i,j in zip(x,y) if i!=j]

def solve(y:list):
    for i in range(len(y)-1):
        found = 1; mis = 0
        for j in range(min(i+1,len(y)-1-i)):
            if y[i-j] != y[i+j+1]:
                if found == len(diff(y[i-j],y[i+j+1]))==1:
                    mis += 1
                else:
                    found = 0
            if found==0 or mis > 1: break
        if found == 1 and mis == 1: return i+1
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
