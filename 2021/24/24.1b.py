c5=[ 1, 1, 1, 1, 26, 26, 1, 26, 1, 26, 1, 26, 26, 26 ]
c6=[ 13, 13, 10, 15, -8, -10, 11, -3, 14, -4, 14, -5, -8, -11 ]
c16=[ 15, 16, 4, 14, 1, 5, 1, 3, 3, 7, 5, 13, 3, 10 ]

def decode(inp):
  z=0
  for i in range(0,14):
    if c5[i]==26: z = z//26
    if inp[i]!=c6[i]+(z%26): z = z*26+inp[i]+c16[i]
  return z

def inputs(n):
  inp=[9 for _ in range(0,n)]
  yield inp
  while True:
    i=n-1
    while i>=0:
      inp[i] = inp[i]-1
      if inp[i]==0: inp[i]=9; i=i-1
      else: break
    yield inp

def base26(z):
  res=[]
  while z>0:
    res.append(z%26)
    z=z//26
  return res[::-1]

c6p16 = [[ c6[i]+c16[j] if j<i else 0 for j in range(0,14)] for i in range(0,14)]
for i in range(len(c6p16)):
  print(i+1, c6p16[i])

for x in inputs(14):
  z=decode(x)
  # print(x,base26(z))
  if z==0: break
