import copy

scanner=[]
with open('input.txt') as f:
  for line in f:
    if line=='\n':
      # print('Scanner %d: %d beacons' % (len(scanner)-1, len(scanner[-1])));
      continue
    if line[0:3]=='---': scanner.append(set()); continue
    x,y,z=line.strip().split(',')[0:3]
    scanner[-1].add((int(x),int(y),int(z)))
    #print('Scanner %d: %d,%d,%d' % (len(scanner)-1,int(x),int(y),int(z)))
  #print('Scanner %d: %d beacons' % (len(scanner)-1, len(scanner[-1])))

def rot_helper(x,y,z,orient):
  if orient==0: return x,y,z
  elif orient==1: return x,z,-y
  elif orient==2: return x,-y,-z
  elif orient==3: return x,-z,y
  elif orient==4: return -x,-y,z
  elif orient==5: return -x,z,y
  elif orient==6: return -x,y,-z
  elif orient==7: return -x,-z,-y

def rotate(p,orient):
  x,y,z=p
  if orient<8: return rot_helper(x,y,z,orient)
  elif orient<16: return rot_helper(y,z,x,orient-8)
  elif orient<24: return rot_helper(z,x,y,orient-16)

def plus(p,q): return (p[0]+q[0],p[1]+q[1],p[2]+q[2])
def minus(p,q): return (p[0]-q[0],p[1]-q[1],p[2]-q[2])

def solve_naive(s1, s2, orient):
  ''' Find placement of s2 wrt s1, given orientation of s2. '''
  for p1 in s1:
    for p2 in s2:
      pr2 = rotate(p2,orient)
      dp = minus(pr2,p1)
      overlap=set()
      for p in s2:
        p = minus(rotate(p,orient),dp)
        if p in s1: overlap.add(p)
      if len(overlap)>=12:
        return True, dp
  return False,(0,0,0)

''' Compute all pairwise point differences for each scanner and orientations. '''
diffs=[[set() for orient in range(24)] for i in range(len(scanner))]
for i in range(len(scanner)):
  for orient in range(24):
    for p1 in scanner[i]:
      for p2 in scanner[i]:
        diffs[i][orient].add(rotate(minus(p2,p1),orient))

''' Use this to detect possible overlap between two scanners, if so find actual overlap. '''
pos2={}
for i in range(0,len(scanner)):
  for j in range(0,len(scanner)):
    if i==j: continue
    for orient in range(24):
      n = len(diffs[i][0].intersection(diffs[j][orient]))
      if n>=12*13/2:
        # print('Potential candidate %d -> %d (orient:%d) have %d displacements in common' % (i,j,orient,n))
        match,dp = solve_naive(scanner[i],scanner[j],orient)
        if match:
          # print('Connection %d -> %d (orient:%d) with displacement %d,%d,%d' % (i,j,orient,dp[0],dp[1],dp[2]))
          pos2[(i,j)] = dp,orient

''' Compute spanning tree rooted at scanner 0 in the graph above. '''
seq=[]; vis=set(); b=[(0,-1)]
while len(b)>0:
  i,k=b.pop(0)
  if i in vis: continue
  seq.append((i,k)); vis.add(i)
  for j in range(0,len(scanner)):
    if (i,j) in pos2: b.append((j,i))
# print(seq)

''' In reverse sequence, add points from children in the spanning tree to each scanner using rotation and translation. '''
seq.pop(0); s=[copy.deepcopy(scanner[i]) for i in range(len(scanner))]
for j,i in seq[::-1]:
  for p in s[j]:
    dp,orient = pos2[(i,j)]
    s[i].add(minus(rotate(p,orient),dp))
print(len(s[0]))
