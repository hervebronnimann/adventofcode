from collections import defaultdict

uni1=defaultdict(int)
# Example: 4,8 (minus 1 to do %10 more easily)
# uni1[(3,0,7,0)]=1 # p1,s1,p2,s2 -> num universes
# Input: 6,2 (minus 1 to do %10 more easily)
uni1[(5,0,1,0)]=1 # p1,s1,p2,s2 -> num universes

count=defaultdict(int)
for d1 in [1,2,3]:
  for d2 in [1,2,3]:
    for d3 in [1,2,3]:
      count[d1+d2+d3]+=1
print(count)

n1=0; n2=0
while True:
  uni2=defaultdict(int)
  for key,n in uni1.items():
    p1,s1,p2,s2 = key
    for d in range(3,10):
      if s1+(p1+d)%10+1>=21:
        n1+=n*count[d]
      else:
        uni2[((p1+d)%10,s1+(p1+d)%10+1,p2,s2)]+=n*count[d]
  if len(uni2)==0:
    print("Player 1,2 wins in %d,%d universes." % (n1,n2))
    break

  uni1=defaultdict(int)
  for key,n in uni2.items():
    p1,s1,p2,s2 = key
    for d in range(3,10):
      if s2+(p2+d)%10+1>=21: n2+=n*count[d]
      else:
        uni1[(p1,s1,(p2+d)%10,s2+(p2+d)%10+1)]+=n*count[d]
  if len(uni1)==0:
    print("Player 2,1 wins in %d,%d universes." % (n2,n1))
    break
