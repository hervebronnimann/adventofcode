import re
input = open("input.txt",'r').read().strip().split('\n\n')

rules = {}
for rule in input[0].split('\n'):
    rule = re.sub('[{},]+', ' ', rule).strip()
    x = rule.split(' ')
    rules[ x[0] ] = x[1:]

def splitRule(r,x,m,a,s):
    x1,x2 = x; m1,m2 = m; a1,a2 = a; s1,s2 = s
    r,t = r.split(':')
    val = int(r[2:])
    if r.startswith('x<'): return [(t,(x1,val-1),m,a,s),((val,x2),m,a,s)]
    if r.startswith('x>'): return [(t,(val+1,x2),m,a,s),((x1,val),m,a,s)]
    if r.startswith('m<'): return [(t,x,(m1,val-1),a,s),(x,(val,m2),a,s)]
    if r.startswith('m>'): return [(t,x,(val+1,m2),a,s),(x,(m1,val),a,s)]
    if r.startswith('a<'): return [(t,x,m,(a1,val-1),s),(x,m,(val,a2),s)]
    if r.startswith('a>'): return [(t,x,m,(val+1,a2),s),(x,m,(a1,val),s)]
    if r.startswith('s<'): return [(t,x,m,a,(s1,val-1)),(x,m,a,(val,s2))]
    if r.startswith('s>'): return [(t,x,m,a,(val+1,s2)),(x,m,a,(s1,val))]
    print("OUCH"); return []

def valid(x): return x[0] <= x[1]

def splitRules(name,x,m,a,s):
    if name == 'A': return [(x,m,a,s)]
    if name == 'R': return []
    L = []
    for r in rules[name]:
        if ':' not in r:
            return L + splitRules(r,x,m,a,s)
        elif valid(x) and valid(m) and valid(a) and valid(s):
            res = splitRule(r,x,m,a,s)
            if len(res) == 2:
                n1,x1,m1,a1,s1 = res[0]
                x,m,a,s = res[1]
                if valid(x1) and valid(m1) and valid(a1) and valid(s1):
                    L += splitRules(n1,x1,m1,a1,s1)
            else:
                L += res
    return L

L = splitRules('in',(1,4000),(1,4000),(1,4000),(1,4000))

def size(x): return x[1] - x[0] + 1 if x[1]>=x[0] else 0

res = 0
for x,m,a,s in L:
    res += size(x) * size(m) * size(a) * size(s)
print(res)
