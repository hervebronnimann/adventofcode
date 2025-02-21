from collections import defaultdict
import itertools

triples = set()
g = defaultdict(list)
for l in open('input.txt').read().strip().split('\n'):
    p,q = l.split('-')
    g[p].append(q)
    g[q].append(p)
for p,pl in g.items():
    if p[0] != 't': continue
    for q,r in itertools.combinations(pl,2):
        if r in g[q]:
            triples.add(tuple(sorted((p,q,r))))
print(len(triples))
