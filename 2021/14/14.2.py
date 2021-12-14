import copy
from collections import defaultdict

poly=""
rules={}
bigrams=defaultdict(lambda: 0)

with open('input.txt') as f:
  poly=next(f).strip()
  for i in range(len(poly)-1):
    bigrams[poly[i]+poly[i+1]] += 1
  next(f)
  for l in f:
    u,v = l.strip().split(' -> ')[0:2]
    rules[u]=v

def mutate(poly):
  global bigrams
  bigrams2=defaultdict(lambda: 0)
  for b in bigrams.keys():
    u,v = list(b)
    if b in rules.keys():
      bigrams2[u+rules[b]] += bigrams[b]
      bigrams2[rules[b]+v] += bigrams[b]
    else:
      bigrams2[b] += bigrams[b]
  bigrams=copy.deepcopy(bigrams2)
    
for i in range(40): mutate(poly)

count=defaultdict(lambda: 0)
count[poly[-1]]=1
for x in list(bigrams): count[x[0]] += bigrams[x]
print(max(count.values()) - min(count.values()))

