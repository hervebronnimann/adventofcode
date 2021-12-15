def cost(a,i): return sum([abs(x-a[i]) for x in a])

with open("input.txt") as f:
  a=[int(x) for x in next(f).split(",")]

i0=0; i1=len(a)-1
while i0+3<i1:
  i2=i0+(i1-i0)//3
  i3=i1-(i1-i0)//3
  m2=cost(a,i2)
  m3=cost(a,i3)
  i0 = i2 if m3<=m2 else i0
  i1 = i3 if m2<=m3 else i1
c=[cost(a,i) for i in range(i0,i1+1)]
print(min(c))
