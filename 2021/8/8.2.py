def solve(inp,outp):
  fmap={}; rmap={}
  def sortString(x): return "".join(sorted(x))
  def mapping(x,t): fmap[sortString(x)]=t; rmap[t]=set(x)
  # First pass
  for x in inp: # 1, 7, 4, or 8
    if len(x)==2: mapping(x,1)
    if len(x)==3: mapping(x,7)
    if len(x)==4: mapping(x,4)
    if len(x)==7: mapping(x,8)
  # Second pass
  for x in inp:
    if len(x)==5: # 2, 3, or 5
      if len(set(x).intersection(rmap[1]))==2: mapping(x,3)
      elif len(set(x).intersection(rmap[4]))==2: mapping(x,2)
      elif len(set(x).intersection(rmap[4]))==3: mapping(x,5)
      else: print(f"Unknown symbol1 {x}")
    elif len(x)==6: # 0, 6, or 9
      if len(set(x).intersection(rmap[1]))==1: mapping(x,6)
      elif len(set(x).intersection(rmap[4]))==4: mapping(x,9)
      elif len(set(x).intersection(rmap[4]))==3: mapping(x,0)
      else: print(f"Unknown symbol2 {x}")
    elif len(x)!=2 and len(x)!=3 and len(x)!=4 and len(x)!=7:
      print(f"Unknown symbol3 {x}")
  # Compute output
  n=0;
  for x in outp:
    if sortString(x) not in fmap.keys(): 
      print(f"Unknown symbol4 {x}")
    n = fmap[sortString(x)] + 10*n
  return n

input=[]
output=[]
with open('input.txt') as f:
  for lline in f:
    line=lline.split()
    input.append([line[i] for i in range(0,10)]);
    output.append([line[i] for i in range(11,15)]);

n=0
for k in range(0,len(input)):
  # print(solve(input[k],output[k]));
  n+=solve(input[k],output[k])
print(n)
