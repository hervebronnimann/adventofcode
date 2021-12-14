from collections import defaultdict

poly=""
rules={}
bigrams=defaultdict(int)

with open('input.txt') as f:
  poly=next(f).strip()
  for i in range(len(poly)-1):
    bigrams[poly[i:i+2]] += 1
  next(f)
  for l in f:
    u,v = l.strip().split(' -> ')[0:2]
    rules[u]=v

def mutate(poly):
  global bigrams
  bigrams2=defaultdict(int)
  for b,k in bigrams.items():
    if b in rules.keys():
      bigrams2[b[0]+rules[b]] += k
      bigrams2[rules[b]+b[1]] += k
    else:
      bigrams2[b] += k
  bigrams=bigrams2
    
for i in range(40): mutate(poly)

count=defaultdict(int)
count[poly[-1]]=1
for x,y in bigrams.items(): count[x[0]] += y
print(max(count.values()) - min(count.values()))

