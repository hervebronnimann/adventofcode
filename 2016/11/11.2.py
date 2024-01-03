from copy import deepcopy
from collections import deque

# Example:
F1 = ['-hydrogen', '-lithium']
F2 = ['+hydrogen']
F3 = ['+lithium']
F4 = []

F1 = ('+promethium', '-promethium','+dilithium','-dilithium','+elerium','-elerium')
F2 = ('+cobalt', '+curium', '+plutonium', '+ruthenium')
F3 = ('-cobalt', '-curium', '-plutonium', '-ruthenium')
F4 = ()

# Manually, mmmh....
# Step 1: +prom to floor 2
# 2 to 5: up cobalt, then curium+plutonium down to floor 2, and ruthenium to 3
# 6 to :

E = 0
F = (F1,F2,F3,F4)

def has_rtg(f):
    for x in f:
        if x[0]=='+': return True
    return False

def valid(f):
    for x in f:
        if x[0]=='-':
            y = '+'+x[1:]
            if y in f: continue
            if has_rtg(f):
                # print(f"Not protected {x}")
                return False
    return True

def endstate(e,f):
    return e==3 and all(len(f[i])==0 for i in [0,1,2])

def powerset2(s):
    n = len(s)
    for i in range(n):
        yield ([x for k,x in enumerate(s) if k==i], [x for k,x in enumerate(s) if k!=i])
    for i in range(n):
        for j in range(i,n):
            yield ([x for k,x in enumerate(s) if k==i or k==j], [x for k,x in enumerate(s) if k!=i and k!=j])

def nextfloor(e,f):
    ne = {0:[1],1:[0,2], 2:[1,3], 3:[2]}[e]
    already1,already2 = 0,0
    for h,nh in powerset2(f[e]):
        for g in ne:
            # Don't carry stuff back to empty floors below.
            if g < e and all(len(f[k])==0 for k in range(0,e)): continue
            # Don't carry one up (or two down) if you already carried two (or one down)
            if g>e and already2 and len(h)==1: continue
            if g<e and already1 and len(h)==2: continue
            y = [ sorted(list(f[x])+h) if x==g else nh if x == e else f[x] for x in [0,1,2,3] ]
            if valid(y[g]) and valid(y[e]):
                if g>e and len(h)==2: already2 = 1
                if g<e and len(h)==1: already1 = 1
                yield (g,y)

def hashpair(f):
    """ The idea is to count the number of matched pairs and keep only the rest """
    n,p = 0,[]
    for x in f:
        if x[0]=='+':
            if '-'+x[1:] in f: n+=1
            else: p += [x]
        elif x[0]=='-':
            if '+'+x[1:] in f: n+=1
            else: p += [x]
    return(n,tuple(p))

def hashable(e,f):
    return (e,hashpair(f[0]),hashpair(f[1]),hashpair(f[2]),hashpair(f[3]))

q = deque([(E,F,0)])
m,visited = 1,set([hashable(E,F)])
while q:
    e,f,i = q.popleft()
    if len(visited)%100==0 and len(visited)>m:
        print("Distance ",i,"Visited ",len(visited))
        m = len(visited)
    # print(f"Now[{i}]: {e} {f}")
    for g,h in nextfloor(e,f):
        # print("Next:",i+1,g,h)
        if endstate(g,h):
            # print("Reaching: step",i+1,g,h)
            print("Part 1:",i+1); q=[]; break
        if hashable(g,h) not in visited:
            # print("Queuing: step",i+1,g,h)
            visited.add(hashable(g,h))
            q.append((g,h,i+1))

print("Visited:",len(visited))
