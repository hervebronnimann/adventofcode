import copy

graph={}
def make_edge(s,d):
  if s not in graph.keys(): graph[s]=[]
  graph[s].append(d)
def make_edge2(s,d):
  if d != 'start': make_edge(s,d)
  if s != 'start': make_edge(d,s)

with open('input.txt') as f:
  for l in f: make_edge2(l.split('-')[0],l.split('-')[1].rstrip('\n'))

paths=['start']
while True:
  # print('Iteration:')
  paths2=[]; new_paths=False
  for p in paths:
    pend = p.split(',')[-1]
    if pend=='end': 
      paths2.append(p)
      continue
    for d in graph[pend]:
      if d.isupper() or p.find(','+d+',')==-1:
        paths2.append(p+','+d)
        new_paths=True
        # print paths2[-1]
  if not new_paths: break
  paths=paths2

# print(paths)
n=0
for p in paths:
  if p.find(',end')==-1: n += 1
print(n)

