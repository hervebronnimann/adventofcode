import copy

poly=""
rules={}
bigrams={}

def incr(b,k,n):
  if k not in b.keys(): b[k]=0
  b[k] += n

with open('input.txt') as f:
  poly=next(f).strip()
  for i in range(len(poly)-1):
    incr(bigrams,poly[i]+poly[i+1],1)
  next(f)
  for l in f:
    u,v = l.strip().split(' -> ')[0:2]
    # print (u+" -> "+v)
    rules[u]=v

def mutate(poly):
  global bigrams
  b2={}
  for b in bigrams.keys():
    u,v = list(b)
    if b in rules.keys():
      w=rules[b]
      incr(b2,u+w,bigrams[b])
      incr(b2,w+v,bigrams[b])
    else:
      incr(b2,b,bigrams[b])
  bigrams=copy.deepcopy(b2)
    
print(poly)
for i in range(40):
  mutate(poly)
  # print("Iter %d: %s" %(i+1,poly))
print(bigrams)

count={poly[-1]:1}
for x in list(bigrams): incr(count,x[0],bigrams[x])
print (count)
print(max(count.values()) - min(count.values()))

