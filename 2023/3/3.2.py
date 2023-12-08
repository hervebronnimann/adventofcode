def adj_stars(M, i, j0, j1):
  ret = set()
  if M[i][j0-1] == '*': ret.add( (i,j0-1) ) 
  if M[i][j1] == '*':  ret.add( (i,j1) ) 
  for j in range(j0-1,j1+1):
    if M[i-1][j] == '*': ret.add( (i-1,j) )
    if M[i+1][j] == '*':  ret.add( (i+1,j) )
  return ret

def find_syms(M, i):
  ret = []; j = 1
  while j < len(M[i])-1:
    if M[i][j].isdigit():
      j1 = j+1
      while M[i][j1].isdigit(): j1 += 1
      ret = ret + [(i,j,j1,int(M[i][j:j1]),adj_stars(M,i,j,j1))]
      j = j1+1
    else:
      j += 1
  return ret

def gear(M, s1, s2):
  return len(s1[4].intersection(s2[4])) > 0
  
res = 0
with open("example.txt",'r') as f:
  M = [ "." + s.strip() + "." for s in f]
  M = ["."*len(M[0])] + M + ["."*len(M[0])]
  S = []
  for i in range(1,len(M)-1):
    S = S + find_syms(M,i)
  for i1 in range(len(S)):
    for i2 in range(i1+1,len(S)):
      if gear(M,S[i1],S[i2]):
        print(S[i1],S[i2])
        res += S[i1][3] * S[i2][3]
print(res)
