from collections import deque
import re
import math
input = open("input.txt",'r').read().strip().split('\n\n')

modules = { 'rx' : ('>',[]) }
state = { 'rx' : 0, 'rxh' : 0 }
endpoints = []  # those nodes who feed into the final '&vr -> rx'

for config in input[0].split('\n'):
    config = re.sub('[,-> ]+', ' ', config).strip()
    x = config.split(' ')
    m = x[0][1:] if x[0] != 'broadcaster' else 'broadcaster'
    type = x[0][0] if x[0] != 'broadcaster' else '='
    modules[m] = (type, x[1:])
    # print(m, type, x[1:])
    if type == '%': state[m] = 'off'
    if type == '&': state[m] = dict()
    if 'vr' in x[1:]: endpoints.append(m)

# Build initial state, for conjunction modules
for m in modules:
    _,dest = modules[m]
    for d in dest:
        if isinstance(state[d], dict):
            state[d][m] = 'low'

# Propagate a signal:
b = { 'low':0, 'high':0 }
cycles = { x:[] for x in endpoints }
def push_button(k):
    sig = deque([('broadcaster','low','button')])
    state['rx'] = 0 ; p = 0
    while sig:
        m,s,i = sig.popleft()
        b[s] += 1; p += 1
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
            if m in endpoints and s2 == 'high':
                cycles[m].append((k,p))
        if type == '>' and s == 'low':
            state['rx'] += 1
        if s2:
            for d in dest: sig.append((d,s2,m))
    return (b['low'],b['high'])

# Brute force takes forever - I've had it run till 155M and not found...
# So looking a bit deeper, found that vr->rx has four ancestors (call them endpoints),
# each of them needing to be high, and looking at their cyclicities,
# they tick exactly at multiples of cycles.
def cycle_detect(N):
    for n in range(1,N+1):
        push_button(n);
        if n == 1000: print(f"Part 1: {b['low']*b['high']}")

cycle_detect(10000)
# print(cycles)
print(f'Part 2: {math.prod(x[0][0] for x in cycles.values())}')
