def find_syms(M, i):
  ret = []; j = 1
  while j < len(M[i])-1:
    if M[i][j].isdigit():
      j1 = j+1
      while M[i][j1].isdigit(): j1 += 1
      ret = ret + [(j,j1)]
      j = j1+1
    else:
      j += 1
  return ret

def adj(M, i, j0, j1):
  if M[i][j0-1] != '.' or M[i][j1] != '.': return 1
  for j in range(j0-1,j1+1):
    if M[i-1][j] != '.' or M[i+1][j] != '.': return 1
  return 0

res = 0
with open("input.txt",'r') as f:
  M = [ "." + s.strip() + "." for s in f]
  M = ["."*len(M[0])] + M + ["."*len(M[0])]
  # print(M)
  for i in range(1,len(M)-1):
    s = find_syms(M,i)
    # print(i,[(j0,j1,adj(M,i,j0,j1)) for (j0,j1) in s])
    res += sum([int(M[i][j0:j1])*adj(M,i,j0,j1) for (j0,j1) in s])

print(res)
