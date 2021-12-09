def digit(x): return ord(x)-ord('0')

with open("input.txt") as f:
  m=0; b={}
  for line in f: n=len(line); m+=1; b[m]='9'+line.rstrip('\n')+'9'
  b[0]='9'*(n+2); b[m+1]='9'*(n+2)

risk=0
for i in range(1,m+1):
  for j in range(1,n+1):
    if b[i][j]<b[i+1][j] and b[i][j]<b[i-1][j] and b[i][j]<b[i][j+1] and b[i][j]<b[i][j-1]:
      # print("Low point %s at [%d,%d]" % (b[i][j],i,j))
      risk += digit(b[i][j])+1
print(risk)
