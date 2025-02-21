from collections import defaultdict

def parse_values(rules):
    values = {}
    for v in rules:
        x,y = v.split(': ')
        values[x] = int(y)
    return values

def parse_rules(rules):
    ops = defaultdict(tuple)
    dag = defaultdict(list)
    for o in rules:
        x,op,y,_,z = o.split()
        if z in ops: raise ValueError('Dual definition of '+z)
        ops[z] = (x,op,y)
        dag[z].extend([x,y])
        if x not in dag: dag[x] = []
        if y not in dag: dag[y] = []
    return ops,dag

def dfs(x,dag,topo,visit):
    if x in topo: return
    if x in visit: raise ValueError('Cycle in graph involving '+y)
    visit.add(x)
    for y in dag[x]:
        dfs(y,dag,topo,visit)
    topo.append(x)

def topo_sort(dag):
    topo = []
    visit = set()
    for x in dag:
        dfs(x,dag,topo,visit)
    return topo

def eval_string(z,ops,depth=-1):
    if z[0] == 'x' or z[0] == 'y' or depth == 0: return z
    x,op,y = ops[z]
    return f"({eval_string(x,ops,depth-1)} {op} {eval_string(y,ops,depth-1)})"

def eval_n(z,ops,depth = -1):
    if z[0] == 'x' or z[0] == 'y' or depth == 0: return set([z])
    x,op,y = ops[z]
    return eval_n(x,ops,depth-1) | eval_n(y,ops,depth-1) | set([x,y])

rules = open('input2.txt').read().strip().split('\n\n')
values = parse_values(rules[0].split('\n'))
ops,dag = parse_rules(rules[1].split('\n'))

xs = [ f'x{n:02d}' for n in range(45)]
ys = [ f'y{n:02d}' for n in range(45)]
bases =  set(xs) | set(ys)
used = set()
for n in range(46):
    s = eval_n(f'z{n:02d}', ops) - bases
    print(f"z{n:02d} evaluates to " + eval_string(f'z{n:02d}', ops, depth=1))
    print(f"   and uses additionally")
    for d in s - used:
        x,op,y = ops[d]
        print(f"    {d} = {x} {op} {y}")
    used |= s
    if set(xs[0:n+1]) | set(ys[0:n+1]) != eval_n(f'z{n:02d}', ops) & bases:
        # print(f"Error with z{n:02d}, evaluates to " + eval_string(f'z{n:02d}', ops))
        print(f"Error with z{n:02d}, uses only " + str(sorted(eval_n(f'z{n:02d}', ops)-bases)))
        print(f"    and z{n:02d} evaluates to " + eval_string(f'z{n:02d}', ops, depth=2))
        print(f"By comparison z{n-1:02d}, uses " + str(sorted(eval_n(f'z{n-1:02d}', ops)-bases)))
        print(f"    and z{n-1:02d} evaluates to " + eval_string(f'z{n-1:02d}', ops, depth=2))
    print('-----------')

