import copy

graph={}
def make_edge(s,d):
  if s not in graph.keys(): graph[s]=[]
  graph[s].append(d)
def make_edge2(s,d):
  if d != 'start' and s != 'end':
    print('Edge '+s+' to '+d)
    make_edge(s,d)
  if s != 'start' and d != 'end':
    print('Edge '+d+' to '+s)
    make_edge(d,s)

with open('input.txt') as f:
  for l in f: make_edge2(l.split('-')[0],l.split('-')[1].rstrip('\n'))

paths={'start':1}
while True:
  # print('Iteration:')
  paths2={}; new_paths=False
  for pstr in paths.keys():
    p = pstr.split(',')
    if p[-1]=='end': 
      paths2[pstr]=paths[pstr]
      continue
    for d in graph[p[-1]]:
      if d.isupper() or p.count(d)<=paths[pstr]:
        paths2[pstr+','+d]=(0 if d.islower() and p.count(d)==1 else paths[pstr])
        new_paths=True
        # print pstr+','+d
  if not new_paths: break
  paths=paths2

print(paths)
n=0
for p in paths.keys():
  if p.find(',end')>=0: n += 1
print(n)

