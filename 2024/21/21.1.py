from collections import defaultdict

codes = open('input.txt').read().strip().split('\n')
codes = open('example.txt').read().strip().split('\n')

# graph for the doors
g_door = {
  '0':(0,1),
  'A':(0,2),
  '1':(1,0),
  '2':(1,1),
  '3':(1,2),
  '4':(2,0),
  '5':(2,1),
  '6':(2,2),
  '7':(3,0),
  '8':(3,1),
  '9':(3,2),
}

# take advantage of Manhattan metric, avoid (0,0)
def sign(x): return 1 if x > 0 else -1 if x < 0 else 0
def move(di,dj): return '<' if dj < 0 else '>' if dj > 0 else 'v' if di < 0 else '^'

def paths(p,q,path_list):
    if p == (0,0): return []
    if p == q: return path_list
    di,dj = sign(q[0]-p[0]),sign(q[1]-p[1])
    result = []
    if di != 0: result += paths((p[0]+di,p[1]),q,[f+move(di,0) for f in path_list])
    if dj != 0: result += paths((p[0],p[1]+dj),q,[f+move(0,dj) for f in path_list])
    return result

# all pairs shortest paths between door positions: enumerate paths (not just length)
g_paths = defaultdict(list)
for i,p in g_door.items():
    for j,q in g_door.items():
        g_paths[i+j] = paths(p,q,[''])
# print(g_paths)

# graph for the directions
g_dir = {
    'A': (0,2),
    '^': (0,1),
    'v': (-1,1),
    '>': (-1,2),
    '<': (-1,0),

}
# all pairs shortest paths between door positions: again,enumerate paths (not just length)
g_dpaths = defaultdict(list)
for i,p in g_dir.items():
    for j,q in g_dir.items():
        g_dpaths[i+j] = paths(p,q,[''])
# print(g_dpaths)


# given a sequence p of directional moves starting/ending with A, what are all the possible ways to accomplish it remotely
def remote(p : str):
    result,a = [''],'A'
    for b in p:
        result = [ p+l+'A' for l in g_dpaths[a+b] for p in result ]
        a = b
    return result

result = 0
for c in codes:
    m,a = [''],'A'
    for b in c:
        m = [ p+l+'A' for l in g_paths[a+b] for p in m]
        a = b
    min_m = min([len(l) for l in m])
    m = [ l for l in m if len(l) == min_m]
    print(f"Code {c} pad robot 1: {min_m} {len(m)} {m}")
    n = []
    for l in m: n.extend( remote(l) )
    min_n =  min([len(l) for l in n])
    n = [ l for l in n if len(l) == min_n]
    print(f"Code {c} pad robot 2: {min_n} {len(n)}")
    o = []
    for l in n: o.extend( remote(l) )
    min_o =  min([len(l) for l in o])
    o = [l for l in o if len(l) == min_o]
    print(f"Code {c} final pad: {min_o}")
    result += min_o * int(c[0:3])
print(result)
