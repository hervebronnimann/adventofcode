import re
input = open("input.txt",'r').read().strip().split('\n\n')

rules = {}
for rule in input[0].split('\n'):
    rule = re.sub('[{},]+', ' ', rule).strip()
    x = rule.split(' ')
    rules[ x[0] ] = x[1:]
print(rules)

def evalRule(r,x,m,a,s):
    if ':' not in r: return r
    r = r.split(':')
    if eval(r[0]): return r[1]
    return None

def evalRules(x,m,a,s):
    name = 'in'; names = []
    while True:
        names.append(name)
        for r in rules[name]:
            res = evalRule(r,x,m,a,s)
            if res:
                if res in 'AR':
                    print(' -> '.join(names + [res]))
                    return res
                name = res; break

res = 0
for part in input[1].split('\n'):
    x,m,a,s = [int(t) for t in re.sub('[^0-9]+', ' ', part).strip().split(' ')]
    if evalRules(x,m,a,s) == 'A': res += x+m+a+s
print(res)

