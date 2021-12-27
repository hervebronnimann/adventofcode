from copy import deepcopy

# I could hardwire it as below, but just to make sure I'm reading them correctly:
c5=[]; c6=[]; c16=[]
with open('input.txt') as f:
  lineno=1
  for l in f:
    if lineno%18==5: c5.append(int(l.strip().split()[-1]))
    if lineno%18==6: c6.append(int(l.strip().split()[-1]))
    if lineno%18==16: c16.append(int(l.strip().split()[-1]))
    lineno+=1
  print(c5)
  print(c6)
  print(c16)

# For my input, this should be the same as:
# c5=[ 1, 1, 1, 1, 26, 26, 1, 26, 1, 26, 1, 26, 26, 26 ]
# c6=[ 13, 13, 10, 15, -8, -10, 11, -3, 14, -4, 14, -5, -8, -11 ]
# c16=[ 15, 16, 4, 14, 1, 5, 1, 3, 3, 7, 5, 13, 3, 10 ]

class Scenario:
  def __init__(self):
    self.z=[]
    self.conds=[]
    self.appends=0
  def add_digit(self,i):
    self.appends += 1
    self.z.append(i)
  def add_cond(self,i,j,eq=True):
    self.conds.append((i,j,eq))
  def clone(self):
    s=Scenario()
    s.z=deepcopy(self.z)
    s.appends=self.appends
    s.conds=deepcopy(self.conds)
    return s
  def conditionss(self):
    for i,j,eq in self.conds:
      yield f'w[{i}]{"=" if eq else "!"}=' + (f'{c6[i]}' if j==-1 else f'{c6[i]+c16[j]}+w[{j}]')
  def __str__(self):
    return f'Scenario {self.z} with {self.appends} appends and conditions {[c for c in self.conditionss()]}'

scenarios=[Scenario()]
for i in range(14):
  ns=len(scenarios)
  for s in range(ns):
    sc=scenarios[s]
    if len(sc.z)>0 and c5[i]==26: sc.z.pop(-1)
    j=-1 if len(sc.z)==0 else sc.z[-1]
    possibly=(j<0 and 1<=c6[i] and c6[i]<=9) or (j>=0 and abs(c6[i]+c16[j])<9)
    if c5[i]==26 and not possibly:
      print(f'This scenario will prevent a solution: {sc}')
    if possibly: # possibly equality is true, in which case don't append
      sc2=sc.clone(); sc2.add_cond(i,j,eq=True)
      scenarios.append(sc2)
    # the other scenario is append i to z
    sc.add_digit(i);
    # if possibly: sc.add_cond(i,j,eq=False)
  print(f'After step i={i}: {len(scenarios)} scenarios (could{"" if c5[i]==26 else " not"} pop)')
  for s in scenarios:
    print(s)

