from collections import deque
import re
input = open("input.txt",'r').read().strip().split('\n\n')

modules = { 'rx' : ('>',[]) }
state = { 'rx' : None }
for config in input[0].split('\n'):
    config = re.sub('[,-> ]+', ' ', config).strip()
    x = config.split(' ')
    m = x[0][1:] if x[0] != 'broadcaster' else 'broadcaster'
    type = x[0][0] if x[0] != 'broadcaster' else '='
    modules[m] = (type, x[1:])
    print(m, type, x[1:])
    if type == '%': state[m] = 'off'
    if type == '&': state[m] = dict()

# Build initial state, for conjunction modules
for m in modules:
    _,dest = modules[m]
    for d in dest:
        if isinstance(state[d], dict):
            state[d][m] = 'low'

# Propagate a signal:
b = { 'low':0, 'high':0 }
def push_button():
    sig = deque([('broadcaster','low','button')])
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
        if s2:
            for d in dest: sig.append((d,s2,m))
    return (b['low'],b['high'])

for _ in range(1000): push_button()
print(b['low']*b['high'])
