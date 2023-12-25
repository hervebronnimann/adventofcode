from collections import deque
import re
input = open("input.txt",'r').read().strip().split('\n\n')

modules = { 'rx' : ('>',[]) }
state = { 'rx' : 0, 'rxh' : 0 }
inputs = { 'rx': set() }

for config in input[0].split('\n'):
    config = re.sub('[,-> ]+', ' ', config).strip()
    x = config.split(' ')
    m = x[0][1:] if x[0] != 'broadcaster' else 'broadcaster'
    type = x[0][0] if x[0] != 'broadcaster' else '='
    modules[m] = (type, x[1:])
    print(m, type, x[1:])
    inputs[m] = set()
    if type == '%': state[m] = 'off'
    if type == '&': state[m] = dict()

# Build initial state, for conjunction modules
for m in modules:
    _,dest = modules[m]
    for d in dest:
        inputs[d].add(m)
        if isinstance(state[d], dict):
            state[d][m] = 'low'

# Propagate a signal:
b = { 'low':0, 'high':0 }
contrib = { x: set() for x in modules }
def push_button():
    sig = deque([('broadcaster','low','button')])
    state['rx'] = 0
    state['rxh'] = 0
    while sig:
        m,s,i = sig.popleft()
        b[s] += 1
        type,dest = modules[m]
        s2 = None
        if type == '=':
            s2 = s
        if type == '%' and s == 'low':
            state[m] = 'off' if state[m] == 'on' else 'on'
            s2 = 'high' if state[m] == 'on' else 'low'
        if type == '&':
            state[m][i] = s
            s2 = 'low' if all(x == 'high' for x in state[m].values()) else 'high'
        if type == '>' and s == 'low':
            state['rx'] += 1
        if type == '>' and s == 'high':
            state['rxh'] += 1
        if s2:
            for d in dest:
                contrib[d].update(contrib[m])
                sig.append((d,s2,m))
    return (b['low'],b['high'])

# This takes forever - I've had it run till 155M and not found...
def brute_force(N):
    n = 0
    while state['rx']!=1 and n <= N:
        n+=1; push_button();
        print(f'After {n}, rx received {state["rx"]} low signals and {state["rxh"]} high signals')
        if n == 1000: print(f"Part 1: {b['low']*b['high']}")
    return n

brute_force(100000)
print(contrib)
