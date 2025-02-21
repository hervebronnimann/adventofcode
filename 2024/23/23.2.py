from collections import defaultdict
import itertools

g = defaultdict(list)
for l in open('input.txt').read().strip().split('\n'):
    p,q = l.split('-')
    g[p].append(q)
    g[q].append(p)

V =sorted( list(g.keys()), cmp = lambda x,y: return len(g[x]) - len(g[y]))

# Algorithm Carraghan & Pardalos
# Function Main
# 2: C∗ ← ∅ // the maximum clique
# 3: Clique(∅, V )
# 4: return C∗
# 5: End function
# 6: Function Clique(set C, set P)
# 7: if (|C| > |C∗|) then
# 8: C∗ ← C
# 9: End if
# 10: if (|C| + |P| > |C∗|) then
# 11: for all p ∈ P in predetermined order, do
# 12: P ← P \ {p}
# 13: C′ ← C union {p}
# 14: P′ ← P inter N(p)
# 15: Clique(C′,P′)
# 16: End for
# 17: End if
# 18: End function

maxC = set()

def clique(C,P):
    if len(C) > len(maxC):
        maxC = C
    if len(C) + len(P) > len(maxC):
        for p in P:


