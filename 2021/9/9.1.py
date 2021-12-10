def digit(x): return ord(x)-ord('0')

with open("input.txt") as f:
  b=['9'+line.rstrip('\n')+'9' for line in f]
  m=len(b); n=len(b[0])-2
  b.insert(0,'9'*(n+2)); b.append('9'*(n+2))

# print("\n".join(b))
neighbors=[(-1,0),(1,0),(0,1),(0,-1)]
print(sum(digit(b[i][j])+1  for i in range(1,m+1) for j in range(1,n+1) \
      if all([b[i][j]<b[i+u][j+v] for (u,v) in neighbors])))
