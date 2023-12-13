input = [ x.split('\n') for x in open("input.txt",'r').read().strip().split('\n\n') ]

def solve(y:list):
    for i in range(len(y)-1):
        y0 = y[i::-1]
        y1 = y[i+1:]
        n = min(len(y0),len(y1))
        if y0[0:n] == y1[0:n]: return i+1
    return 0

def transpose(y:list):
  return ["".join(x) for x in zip(*y)]

print( sum([100*solve(x) + solve(transpose(x)) for x in input]) )
