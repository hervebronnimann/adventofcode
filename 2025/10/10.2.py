import itertools

def ints(l): return [ int(x) for x in l.split(',') ]
def ssum(yj):
    n,m = len(yj[0]),len(yj)
    return [ sum([y[i] for y in yj]) for i in range(n) ]
def pprod(xj,b):
    return [ xj*b[i] for i in range(len(b)) ]

def solveRecursive(joltage, bb, n, m, smin, smax, subset, j, sss):
    """ Same as exhaustive, except use branch and bound instead of itertools.product. """
    if j == m:
        if joltage == ssum([pprod(subset[j],bb[j]) for j in range(m)]):
            print(f'Created {joltage} using {sum(subset)}={[subset[i] for i in range(m) if subset[i]>0]} buttons {[bb[i] for i in range(m) if subset[i]>0]}')
            return min(smin, sum(subset)),max(smax,sum(subset))
        return 9999999999999,0
    if sum(subset)>smin: # or sum(subset)<smax:
        return smin,smax # this is where branch-and-bound would apply, but doesn't work with itertools.product.
    ss,ssn = list(subset),sum(subset)
    ranges_j = min([joltage[i] - sss[i] for i in range(n) if bb[j][i] > 0])
    while ss[j] <= ranges_j and ssn <= smin: # and ssn >= smax:
        s = solveRecursive(joltage, bb, n, m, smin, smax, ss, j+1, [sss[i] + ss[j]*bb[j][i] for i in range(n)])
        smin,smax =  min(s[0], smin),max(s[1], smax)
        ss[j],ssn = ss[j]+1,ssn+1
    return smin,smax

def solveBranchAndBound(joltage, bb):
    """ bb is a collection of n-tuples, each one is a button with 0/1 components, and joltage is a n-tuple. """
    smin,smax,n,m = 9999999999999,0,len(joltage),len(bb)
    ranges = [ (1+min([joltage[i] for i in range(n) if b[i]==1])) for b in bb ]
    print(f'Creating {joltage} using {bb}')
    return solveRecursive(joltage, bb, n, m, smin, smax, [0]*m, 0, [0]*n)

def solveExhaustive(joltage, bb):
    """ bb is a collection of n-tuples, each one is a button with 0/1 components, and joltage is a n-tuple. """
    s,n,m = 9999999999999,len(joltage),len(bb)
    ranges = [ range(1+min([joltage[i] for i in range(n) if b[i]==1])) for b in bb ]
    print(f'Creating {joltage} using {bb}')
    for subset in itertools.product(*ranges):
        if sum(subset)>s: continue  # this is where branch-and-bound would apply, but doesn't work with itertools.product.
        p = ssum([pprod(subset[j],bb[j]) for j in range(m)])
        if p == joltage:
                print(f'Created {joltage} using {sum(subset)}={[subset[i] for i in range(m) if subset[i]>0]} buttons {[bb[i] for i in range(m) if subset[i]>0]}')
                s = min(s,sum(subset))
    return s


sol = 0
for l in open('example.txt','r'):
    x=l.strip().split(' ')
    pattern,buttons,joltage = x[0],x[1:-1],x[-1]
    pattern = pattern[1:-1]
    buttons = [ set(ints(x[1:-1])) for x in buttons ]
    buttons = [ [1 if i in bb else 0 for i in range(len(pattern))] for bb in buttons ]
    joltage = ints(joltage[1:-1])
    if len(buttons)>=len(joltage):
        print(f"SIMPLE: {len(buttons)} buttons, {len(joltage)} constraints.")
    else:
        print(f"COMPLEX: {len(joltage)-len(buttons)} degrees of freedom, {len(buttons)} buttons, {len(joltage)} constraints.")
    # sol += solveExhaustive(joltage,buttons)
    sol += solveBranchAndBound(joltage,buttons)[0]
print(sol)
