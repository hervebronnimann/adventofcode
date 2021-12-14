import copy

poly=""
rules={}
with open('input.txt') as f:
# with open('input.txt') as f:
  poly=next(f).strip()
  next(f)
  for l in f:
    u,v = l.strip().split(' -> ')[0:2]
    # print (u+" -> "+v)
    rules[u]=v

def mutate(poly):
  result=""
  for i in range(len(poly)-1):
    result += poly[i]
    if poly[i]+poly[i+1] in rules.keys():
      # print("Apply rule "+(poly[i]+poly[i+1])+" -> "+ rules[poly[i]+poly[i+1]])
      result += rules[poly[i]+poly[i+1]]
  result += poly[-1]
  return result
    
print(poly)
for i in range(10):
  poly=mutate(poly)
  # print("Iter %d: %s" %(i+1,poly))

count={}
for x in list(poly):
  if x not in count.keys(): count[x]=0
  count[x] += 1
# print (count)
print(max(count.values()) - min(count.values()))

