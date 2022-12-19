def p(l,k): return int(l[k])
def parse(l): l=l.split(' '); return (p(l,1), p(l,6), p(l,12),  p(l,18),  p(l,21), p(l,27),  p(l,30))
# lines = list(map(parse, open("example.txt").read().strip().split('\n')))
lines = list(map(parse, open("input.txt").read().strip().split('\n')))
lines=lines[0:3]
print(lines)

# BLUEPRINT: 0:n_print, 1:cost_ore, 2:cost_clay 3:cost_obs_ore 4:cost_obs_clay 5:cost_geode_ore 6:cost_geode_obs
# STATE: 0:minute 1:n_ore, 2:n_clay, 3:n_nobs, 4:n_geode, 5:ore, 6:clay, 7:obs, 8:geode 9:list of minute producing clay robots (to roll back)

def production(s): s[0]+=1; s[5]+=s[1]; s[6]+=s[2]; s[7]+=s[3]; s[8]+=s[4]; return s
def create_geode_robot(s,b): t = list(s); t[7]-=b[6]; t[5]-=b[5]; t=production(t); t[4]+=1; return t
def create_obs_robot(s,b): t = list(s); t[6]-=b[4]; t[5]-=b[3]; t=production(t); t[3]+=1; return t
def create_clay_robot(s,b): t = list(s); t[5]-=b[2]; t=production(t); t[2]+=1; return t
def create_ore_robot(s,b): t = list(s); t[5]-=b[1]; t=production(t); t[1]+=1; return t

def dominated(s1,s2):
  for i in range(4):
    if s1[i] > s2[i]: return False
  return True

def qappend(dr,ds,q,qm,s):
  if s[0]==33: qm.append(s[8]); return
  # first prune fully dominated set - s[5:9] is the set of resources availables
  t1 = tuple(s[1:5]); t2 = tuple(s[5:9])
  if t1 in dr:
    for s2 in dr[t1]:
      if dominated(t2,s2): return  # we have same number of robots and fewer resources
  else:
    dr[t1]=[] 
  # if t2 in ds:
  #   for s1 in ds[t2]:
  #     if dominated(t1,s1): return  # we have same number of resources and fewer robots
  # else:
  #   ds[t2]=[] 
  dr[t1].append(t2)
  # ds[t2].append(t1)
  q.append(s)

def geode(b):
  print(f'Blueprint {b[0]}')
  b35 = max(b[5],b[3])
  m, n, q, qm = 0, 0, [[1,1,0,0,0,0,0,0,0]], []
  dr,ds = dict(),dict()
  while n < len(q):
    s=q[n]; n+=1  # pop
    if m!=s[0]:
      m=s[0]; print(f'  ...minute {m} ({n}, pruning: {len(dr)}/{sum([len(t) for _,t in dr.items()])} {len(ds)}/{sum([len(t) for _,t in ds.items()])})')
      q=q[n:]; n=0
      # dr,ds=dict(),dict()
    # print(f'Min {s[0]}: robots ore {s[1]} clay {s[2]} obs {s[3]} geode {s[4]},\t ore {s[5]} clay {s[6]} obs {s[7]} geode {s[8]}')
    # robot production - four choices, or a choice to do nothing
    # we dont need more robots that we can spend (since we can only build one robot per turn)
    if b[6]<=s[7] and b[5]<=s[5] and m<32: qappend(dr,ds,q,qm,create_geode_robot(s,b))
    if b[4]<=s[6] and b[3]<=s[5] and s[3]<=b[6] and m<32: qappend(dr,ds,q,qm,create_obs_robot(s,b))
    if b[2]<=s[5] and s[2]<=b[4] and m<32: qappend(dr,ds,q,qm,create_clay_robot(s,b))
    if b[1]<=s[5] and s[1]<=b35 and m<32: qappend(dr,ds,q,qm,create_ore_robot(s,b)) 
    qappend(dr,ds,q,qm,production(s))
  print(max(qm))
  return max(qm)
  
g=[(geode(b)) for b in lines]
print(g[0]*g[1])
# print(g[0]*g[1]*g[2])
