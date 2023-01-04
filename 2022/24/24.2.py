import re
from copy import deepcopy

example=0
lines=open("example.txt" if example else "input.txt").read().strip().split('\n')

grid=[]
M,i=0,0
bliz=list()
for x in lines:
  M=len(x)
  grid.append(list(re.sub('[v><^]','.',x)))
  for j in range(M):
    if x[j]=='#': bliz.append((x[j],i,j,0,0))
    elif x[j]=='>': bliz.append((x[j],i,j,0,1))
    elif x[j]=='<': bliz.append((x[j],i,j,0,-1))
    elif x[j]=='^': bliz.append((x[j],i,j,-1,0))
    elif x[j]=='v': bliz.append((x[j],i,j,1,0))
  i+=1
N,M=i-1,M-1

def move_bliz(bliz):
  b = set()
  for n in range(len(bliz)):
    x,i,j,di,dj = bliz[n]
    i+=di; j+=dj
    if x!='#':
      i = 1 if i==N else N-1 if i==0 else i
      j = 1 if j==M else M-1 if j==0 else j
    bliz[n] = (x,i,j,di,dj)
    b.add((i,j))
  return b

def solve(bliz):
  n,q=0,[(0,1,0)]
  while len(q)>0:
    n += 1
    b = move_bliz(bliz)
    q2=set()
    for i,j,m in q:
      for di,dj in (0,0), (1,0), (-1,0), (0,1), (0,-1):
        dm=0
        if i+di<0 or i+di>N or j+dj<1 or j+dj>=M: continue
        if (i+di,j+dj) in b: continue
        if i+di==0:
          if j+dj!=1: continue
          if m==1 and (di,dj)!=(0,0): dm=1
        if i+di==N:
          if j+dj!=M-1: continue
          if m==2: return n
          if m==0 and (di,dj)!=(0,0): dm=1
        q2.add((i+di,j+dj,m+dm))
    q=q2

print(solve(bliz))
