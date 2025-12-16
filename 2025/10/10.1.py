import itertools

def ints(l): return [ int(x) for x in l.split(',') ]

def solve(p, bb):
    n = len(p)
    bbb = [i for i in range(len(bb))]
    for s in range(n):
        for subset in itertools.combinations(bbb,s):
            pp = [0 for _ in range(n)]
            for x in set(subset):
                for i in bb[x]:
                    pp[i] += 1
            q = ''.join([ '#' if pp[i]%2==1 else '.' for i in range(n) ])
            if p == q:
                print(f'Created {p} using {s} buttons {[bb[x] for x in subset]}')
                return s
    print(f'Could not solve {p} with buttons {bb}')
    return 0


sol = 0
for l in open('input.txt','r'):
    x=l.strip().split(' ')
    pattern,buttons,joltage = x[0],x[1:-1],x[-1]
    pattern = pattern[1:-1]
    buttons = [ ints(x[1:-1]) for x in buttons ]
    sol += solve(pattern,buttons)
print(sol)
