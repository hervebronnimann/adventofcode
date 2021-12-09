import numpy as np


def solve(inp,outp):
  fmap={}; rmap={}
  def sort_string(x): return "".join(sorted(x))
  def mapping(x,t): fmap[sort_string(x)]=t; rmap[t]=set(x)
  # First pass
  len_to_symbol={ 2:1, 3:7,4:4, 7:8 }
  for x in inp: # 1, 7, 4, or 8
    if len(x) in len_to_symbol.keys(): mapping(x,len_to_symbol[x])
  # Second pass
  for x in inp:
    if len(x)==5: # 2, 3, or 5
      if len(set(x) & rmap[1])==2: mapping(x,3)
      elif len(set(x) & rmap[4])==2: mapping(x,2)
      elif len(set(x) & rmap[4])==3: mapping(x,5)
      else: print(f"Unknown symbol1 {x}")
    elif len(x)==6: # 0, 6, or 9
      if len(set(x) & rmap[1])==1: mapping(x,6)
      elif len(set(x) & rmap[4])==4: mapping(x,9)
      elif len(set(x) & rmap[4])==3: mapping(x,0)
      else: print(f"Unknown symbol2 {x}")
    elif len(x) not in len_to_symbol.keys():
      print(f"Unknown symbol3 {x}")
  # Compute output
  n=0;
  for x in outp:
    if sort_string(x) not in fmap.keys(): 
      print(f"Unknown symbol4 {x}")
    n = fmap[sort_string(x)] + 10*n
  return n

input=[]
output=[]
with open('input.txt') as f:
  for line in f:
    input.append(line.split('|')[0].split())
    output.append(line.split('|')[1].split())

print(np.sum([solve(input[k],output[k]) for k in range(0,len(input))]))
