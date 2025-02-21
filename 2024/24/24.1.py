from collections import defaultdict

rules = open('input.txt').read().strip().split('\n\n')

values = {}
for v in rules[0].split('\n'):
    x,y = v.split(': ')
    values[x] = int(y)

ops = defaultdict(tuple)
dag = defaultdict(list)
for o in rules[1].split('\n'):
    x,op,y,_,z = o.split()
    if z in ops: raise 'Dual definition of '+z
    ops[z] = (x,op,y)
    dag[z].extend([x,y])
    if x not in dag: dag[x] = []
    if y not in dag: dag[y] = []
print(dag)

visit = set()
topo = []
def dfs(x,dag):
    if x in topo: return
    if x in visit: raise 'Cycle in graph involving '+y
    visit.add(x)
    for y in dag[x]:
        dfs(y,dag)
    topo.append(x)

for x in dag:
    dfs(x,dag)
print(visit)
print(topo)

for z in topo:
    if z[0] == 'x': continue
    if z[0] == 'y': continue
    x,op,y = ops[z]
    if op == 'AND':
        values[z] = 1 if values[x]==1 and values[y]==1 else 0
    elif op == 'OR':
        values[z] = 1 if values[x]==1 or values[y]==1 else 0
    elif op == 'XOR':
        values[z] = 1 if (values[x]==1) != (values[y]==1) else 0
    else:
        raise 'Unknown operation '+op

r = 0
for z in sorted(ops,reverse=True):
    if z[0] == 'z':
        r = r * 2 + values[z]
print(r)
