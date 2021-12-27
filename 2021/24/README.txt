Rewritten the input looks like (from left to right, one column at a time):

    COL 1     COL 2     COL 3     COL 4     COL 5     COL 6     COL 7     COL 8     COL 9     COL 10    COL 11    COL R12   COL R13   COL R14
1.  inp w     inp w     inp w     inp w     inp w     inp w     inp w     inp w     inp w     inp w     inp w     inp w     inp w     inp w
2.  mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0   mul x 0
3.  add x z   add x z   add x z   add x z   add x z   add x z   add x z   add x z   add x z   add x z   add x z   add x z   add x z   add x z
4.  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26  mod x 26
5.  div z 1   div z 1   div z 1   div z 1   div z 26  div z 26  div z 1   div z 26  div z 1   div z 26  div z 1   div z 26  div z 26  div z 26
6.  add x 13  add x 13  add x 10  add x 15  add x -8  add x -10 add x 11  add x -3  add x 14  add x -4  add x 14  add x -5  add x -8  add x -11
7.  eql x w   eql x w   eql x w   eql x w   eql x w   eql x w   eql x w   eql x w   eql x w   eql x w   eql x w   eql x w   eql x w   eql x 8
8.  eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0   eql x 0
9.  mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0
10. add y 25  add y 25  add y 25  add y 25  add y 25  add y 25  add y 25  add y 25  add y 25  add y 25  add y 25  add y 25  add y 25  add y 25
11. mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x
12. add y 1   add y 1   add y 1   add y 1   add y 1   add y 1   add y 1   add y 1   add y 1   add y 1   add y 1   add y 1   add y 1   add y 1
13. mul z y   mul z y   mul z y   mul z y   mul z y   mul z y   mul z y   mul z y   mul z y   mul z y   mul z y   mul z y   mul z y   mul z y
14. mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0   mul y 0
15. add y w   add y w   add y w   add y w   add y w   add y w   add y w   add y w   add y w   add y w   add y w   add y w   add y w   add y w
16. add y 15  add y 16  add y 4   add y 14  add y 1   add y 5   add y 1   add y 3   add y 3   add y 7   add y 5   add y 13  add y 3   add y 10
17. mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x   mul y x
18. add z y   add z y   add z y   add z y   add z y   add z y   add z y   add z y   add z y   add z y   add z y   add z y   add z y   add z y

Call f(w,z,c5,c6,c16) the operation in one column, with the constants that vary in lines 5, 6, and 16.
Note that line 1 resets w, line 2 resets x, and line 9 resets y, so the only value that gets carried
over from column to column is z. Note that c6 can be negative, but z can never be negative,
as you'll see below. Besides, the problem says not to worry.  

Initially, z is 0.  With each w in the range 1:9 (incl.), each column is
equivalent to the program z=f(w,z,...); here f() returns: 

  x=z%26; z/=c5; x+=c6; x=(x!=w); z*=25*x+1; z+=(w+c16)*x; return z

Note that c5=1 or 26.  Also note that c6<0 if c5==26, and c6>0 if c5==1.

So it all hinges on whether x==0 or x==1. Note that x=z%26+c6 prior to comparing with w.
If x==0 (meaning, w==z%26+c6): then z is unchanged.
Else if x==1 (meaning, w!=z%26+c6): then z = z*26 + (w+c16).

We can now start a brute force, which will never finish (likely) but that seems to be the thing to try.

  c5=[ 1,  1,  1,  1,  26, 26,  1,  26, 1,  26, 1,  26, 26, 26 ]
  c6=[ 13, 13, 10, 15, -8, -10, 11, -3, 14, -4, 14, -5, -8, -11 ]
  c16=[15, 16, 4,  14, 1,  5,   1,  3,  3,  7,  5,  13, 3,  10 ]

  def decode(w):
    z=0
    for i in range(0,14):
      if c5[i]==26: z = z//26
      if w[i]!=c6[i]+(z%26): z = z*26+w[i]+c16[i]
    return z

This is done in 24.1b.py, and of course leads nowhere, but printing what it's doing is instructive.
So now if you look at things, and print returned z as a 26-based number, it's obvious it has at most 7 "digits".
So we can rewrite the code above as treating z in base 26:

  def decode26(w):
    z=[]
    for i in range(0,14):
      if c5[i]==26: z.pop() // pop happens exactly 7 times out of 14
      ztop = 0 if len(z)==0 else z[-1]
      if w[i]!=c6[i]+ztop: z.append(w[i]+c16[i])
    return len(z)==0

Note that z[-1] is necessarily w[j]+c16[j] for some j<i, which is always greater than 0.
Also note that w[j]+c16[j]<=9+max(c16)=9+16=25, so there is really no overflow for 26-digits.
So to get z==0 at the end (which means an empty z array), we should append only at most 7 times.
Note that we pop on steps i = 4, 5, 7, 9, 11, 12, 13, but we don't have to not append on those steps.

So we always compare w[i] and c6[i]+w[j]+c16[j], we can print the matrix c6[i]+c16[j]:

i j:0   1   2   3   4   5   6   7    8   9   10  11  12 13
0  [0,  0,  0,  0,  0,  0,  0,   0,  0,  0,  0,  0,  0, 0]
1  [28, 0,  0,  0,  0,  0,  0,   0,  0,  0,  0,  0,  0, 0]
2  [25, 26, 0,  0,  0,  0,  0,   0,  0,  0,  0,  0,  0, 0]
3  [30, 31, 19, 0,  0,  0,  0,   0,  0,  0,  0,  0,  0, 0]
4  [7,  8,  -4, 6,  0,  0,  0,   0,  0,  0,  0,  0,  0, 0]
5  [5,  6,  -6, 4,  -9, 0,  0,   0,  0,  0,  0,  0,  0, 0]
6  [26, 27, 15, 25, 12, 16, 0,   0,  0,  0,  0,  0,  0, 0]
7  [12, 13, 1,  11, -2, 2,  -2,  0,  0,  0,  0,  0,  0, 0]
8  [29, 30, 18, 28, 15, 19, 15,  17, 0,  0,  0,  0,  0, 0]
9  [11, 12, 0,  10, -3, 1,  -3,  -1, -1, 0,  0,  0,  0, 0]
10 [29, 30, 18, 28, 15, 19, 15,  17, 17, 21, 0,  0,  0, 0]
11 [10, 11, -1, 9,  -4, 0,  -4,  -2, -2, 2,  0,  0,  0, 0]
12 [7,  8,  -4, 6,  -7, -3, -7,  -5, -5, -1, -3, 5,  0, 0]
13 [4,  5,  -7, 3, -10, -6, -10, -8, -8, -4, -6, 2, -8, 0]

When that matrix has an (i,i) that is greater than 8 (or less than -8), it's
impossible for w[i] and w[j] to satisfy the comparison, so we always append.

Looking at i=0, it's guaranteed we append for i=0 (because w[0]!=c6[0]==13 since w is in range 1..9 only).
Looking at i=1, j=0, it's guaranteed we append for i=1 (because w[1]!=w[0]+28, since w is in range 1..9 only).
Likewise, we append at i=2, and i=3.

Now for i=4, we pop (remember?) so the top of z is w[2]+c16[2]=w[2]+4.
We don't append if w[4]==w[2]-4 (since c6[4]==-8)], but we could append otherwise.

For i=5, we pop again (the value at the top was either w[4]+c16[4], or w[2]+4).
So we either compare w[5] to w[2]-6 if we did append at i=4, or to w[1]+6
if we did not append at i==4.

We can continue like this at every step, and accumulate scenarios by either appending or not appending.
There ought to be 2^14 scenarios, but much fewer since first 4 digits are always appending, so 2^10.
A scenario consists of the state of the stack z (encoded for simplicity as indices [...,j,...]
instead of w[j]+c16[j], since w is unknown) and a set of conditions or the form:
either w[i]==c6[i]+c16[j]+w[j] or !=, where j is at the top of the stack.
Also when comparing to the top of the stack, we can make a decision if c6[i]+c16[j]<=-9 or >=9, since digits are 1..9.
At the end we can report the scenarios for which the stack is empty.

One thing is for sure, we don't want to append in the last instruction, but
that means w[13] is either w[12]-8, or w[11]+2 if we didn't append for i=12, or w[10]-6, etc.
We don't know the last condition unless we know the whole scenario before hand.

So here's the whole code I come up with:

  # For my input:
  c5=[ 1, 1, 1, 1, 26, 26, 1, 26, 1, 26, 1, 26, 26, 26 ]
  c6=[ 13, 13, 10, 15, -8, -10, 11, -3, 14, -4, 14, -5, -8, -11 ]
  c16=[ 15, 16, 4, 14, 1, 5, 1, 3, 3, 7, 5, 13, 3, 10 ]

  class Scenario:
    def __init__(self):
      self.z=[]
      self.conds=[]
    def add_cond(self,i,j,eq=True):
      self.conds.append((i,j,eq))
    def clone(self):
      s=Scenario()
      s.z=deepcopy(self.z)
      s.conds=deepcopy(self.conds)
      return s
    def conditions(self):
      for i,j,eq in self.conds:
        yield f'w[{i}]{"=" if eq else "!"}=' + (f'{c6[i]}' if j==-1 else '{c6[i]+c16[j]}+w[{j}]')
    def __str__(self):
      return f'Scenario {self.z} with conditions {[c for c in self.conditions()]}'

  scenarios=[Scenario()]
  for i in range(14):
    ns=len(scenarios)
    for s in range(ns):
      sc=scenarios[s]
      if len(sc.z)>0 and c5[i]==26: sc.z.pop()
      j=-1 if len(sc.z)==0 else sc.z[-1]
      eq_possibly=(j<0 and 1<=c6[i] and c6[i]<=9) or (j>=0 and abs(c6[i]+c16[j])<9)
      if eq_possibly: # possibly equality is true, in which case don't append
        sc2=sc.clone(); sc2.add_cond(i,j,eq=True)
        scenarios.append(sc2)
      # the other scenario is to append i to z
      sc.z.append(i);
      if eq_possibly: sc.add_cond(i,j,eq=False)
    print(f'After step i={i}:')
    for s in scenarios:
      print(s)

At the end, we get scenarios ending with a stack z that is always non-empty, containing some w[j]+c16[j].
So all of these have to be 0.  But that's not possible.

And after looking carefully at the code, I find the one scenario which could possibly append but did not
is i==5, j==1, and c6[5]+c16[1]==27...  Looking again in the above matrix, I see entries larger than 26.
But I don't know what that means or if it's an indication that w ought to be more than a single digit.
I maybe should reread the Day 24.  But I don't see it...  FYI, here's the output 

[1, 1, 1, 1, 26, 26, 1, 26, 1, 26, 1, 26, 26, 26]
[13, 13, 10, 15, -8, -10, 11, -3, 14, -4, 14, -5, -8, -11]
[15, 16, 4, 14, 1, 5, 1, 3, 3, 7, 5, 13, 3, 10]

After step i=0: 1 scenarios (could not pop)
Scenario [0] with 1 appends and conditions []

After step i=1: 1 scenarios (could not pop)
Scenario [0, 1] with 2 appends and conditions []

After step i=2: 1 scenarios (could not pop)
Scenario [0, 1, 2] with 3 appends and conditions []

After step i=3: 1 scenarios (could not pop)
Scenario [0, 1, 2, 3] with 4 appends and conditions []

After step i=4: 2 scenarios (could pop)
Scenario [0, 1, 2, 4] with 5 appends and conditions []
Scenario [0, 1, 2] with 4 appends and conditions ['w[4]==-4+w[2]']

After step i=5: 4 scenarios (could pop)
Scenario [0, 1, 2, 5] with 6 appends and conditions []
Scenario [0, 1, 5] with 5 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2] with 5 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1] with 4 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']

After step i=6: 4 scenarios (could not pop)
Scenario [0, 1, 2, 5, 6] with 7 appends and conditions []
Scenario [0, 1, 5, 6] with 6 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2, 6] with 6 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1, 6] with 5 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']
This scenario will prevent a solution: Scenario [0, 1] with 5 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']

After step i=7: 7 scenarios (could pop)
Scenario [0, 1, 2, 5, 7] with 8 appends and conditions []
Scenario [0, 1, 5, 7] with 7 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2, 7] with 7 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1, 7] with 6 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']
Scenario [0, 1, 2, 5] with 7 appends and conditions ['w[7]==2+w[5]']
Scenario [0, 1, 5] with 6 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]']
Scenario [0, 1, 2] with 6 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]']

After step i=8: 7 scenarios (could not pop)
Scenario [0, 1, 2, 5, 7, 8] with 9 appends and conditions []
Scenario [0, 1, 5, 7, 8] with 8 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2, 7, 8] with 8 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1, 7, 8] with 7 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']
Scenario [0, 1, 2, 5, 8] with 8 appends and conditions ['w[7]==2+w[5]']
Scenario [0, 1, 5, 8] with 7 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]']
Scenario [0, 1, 2, 8] with 7 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]']

After step i=9: 14 scenarios (could pop)
Scenario [0, 1, 2, 5, 7, 9] with 10 appends and conditions []
Scenario [0, 1, 5, 7, 9] with 9 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2, 7, 9] with 9 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1, 7, 9] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']
Scenario [0, 1, 2, 5, 9] with 9 appends and conditions ['w[7]==2+w[5]']
Scenario [0, 1, 5, 9] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]']
Scenario [0, 1, 2, 9] with 8 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]']
Scenario [0, 1, 2, 5, 7] with 9 appends and conditions ['w[9]==-1+w[7]']
Scenario [0, 1, 5, 7] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 7] with 8 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 7] with 7 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 5] with 8 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 5] with 7 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 2] with 7 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]']

After step i=10: 14 scenarios (could not pop)
Scenario [0, 1, 2, 5, 7, 9, 10] with 11 appends and conditions []
Scenario [0, 1, 5, 7, 9, 10] with 10 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2, 7, 9, 10] with 10 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1, 7, 9, 10] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']
Scenario [0, 1, 2, 5, 9, 10] with 10 appends and conditions ['w[7]==2+w[5]']
Scenario [0, 1, 5, 9, 10] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]']
Scenario [0, 1, 2, 9, 10] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]']
Scenario [0, 1, 2, 5, 7, 10] with 10 appends and conditions ['w[9]==-1+w[7]']
Scenario [0, 1, 5, 7, 10] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 7, 10] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 7, 10] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 5, 10] with 9 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 5, 10] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 2, 10] with 8 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]']

After step i=11: 28 scenarios (could pop)
Scenario [0, 1, 2, 5, 7, 9, 11] with 12 appends and conditions []
Scenario [0, 1, 5, 7, 9, 11] with 11 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2, 7, 9, 11] with 11 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1, 7, 9, 11] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']
Scenario [0, 1, 2, 5, 9, 11] with 11 appends and conditions ['w[7]==2+w[5]']
Scenario [0, 1, 5, 9, 11] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]']
Scenario [0, 1, 2, 9, 11] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]']
Scenario [0, 1, 2, 5, 7, 11] with 11 appends and conditions ['w[9]==-1+w[7]']
Scenario [0, 1, 5, 7, 11] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 7, 11] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 7, 11] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 5, 11] with 10 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 5, 11] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 2, 11] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]']
Scenario [0, 1, 2, 5, 7, 9] with 11 appends and conditions ['w[11]==2+w[9]']
Scenario [0, 1, 5, 7, 9] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 7, 9] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 7, 9] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 5, 9] with 10 appends and conditions ['w[7]==2+w[5]', 'w[11]==2+w[9]']
Scenario [0, 1, 5, 9] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 9] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 5, 7] with 10 appends and conditions ['w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 5, 7] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 2, 7] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 7] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 2, 5] with 9 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]']
Scenario [0, 1, 5] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]']
Scenario [0, 1, 2] with 8 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[11]==-1+w[2]']

After step i=12: 56 scenarios (could pop)
Scenario [0, 1, 2, 5, 7, 9, 12] with 13 appends and conditions []
Scenario [0, 1, 5, 7, 9, 12] with 12 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2, 7, 9, 12] with 12 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1, 7, 9, 12] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']
Scenario [0, 1, 2, 5, 9, 12] with 12 appends and conditions ['w[7]==2+w[5]']
Scenario [0, 1, 5, 9, 12] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]']
Scenario [0, 1, 2, 9, 12] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]']
Scenario [0, 1, 2, 5, 7, 12] with 12 appends and conditions ['w[9]==-1+w[7]']
Scenario [0, 1, 5, 7, 12] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 7, 12] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 7, 12] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 5, 12] with 11 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 5, 12] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 2, 12] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]']
Scenario [0, 1, 2, 5, 7, 12] with 12 appends and conditions ['w[11]==2+w[9]']
Scenario [0, 1, 5, 7, 12] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 7, 12] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 7, 12] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 5, 12] with 11 appends and conditions ['w[7]==2+w[5]', 'w[11]==2+w[9]']
Scenario [0, 1, 5, 12] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 12] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 5, 12] with 11 appends and conditions ['w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 5, 12] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 2, 12] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 12] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 2, 12] with 10 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]']
Scenario [0, 1, 12] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]']
Scenario [0, 1, 12] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[11]==-1+w[2]']
Scenario [0, 1, 2, 5, 7, 9] with 12 appends and conditions ['w[12]==-1+w[9]']
Scenario [0, 1, 5, 7, 9] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[12]==-1+w[9]']
Scenario [0, 1, 2, 7, 9] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[12]==-1+w[9]']
Scenario [0, 1, 7, 9] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[12]==-1+w[9]']
Scenario [0, 1, 2, 5, 9] with 11 appends and conditions ['w[7]==2+w[5]', 'w[12]==-1+w[9]']
Scenario [0, 1, 5, 9] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[12]==-1+w[9]']
Scenario [0, 1, 2, 9] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[12]==-1+w[9]']
Scenario [0, 1, 2, 5, 7] with 11 appends and conditions ['w[9]==-1+w[7]', 'w[12]==-5+w[7]']
Scenario [0, 1, 5, 7] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]']
Scenario [0, 1, 2, 7] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]']
Scenario [0, 1, 7] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]']
Scenario [0, 1, 2, 5] with 10 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[12]==-3+w[5]']
Scenario [0, 1, 5] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[12]==-3+w[5]']
Scenario [0, 1, 2] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[12]==-4+w[2]']
Scenario [0, 1, 2, 5, 7] with 11 appends and conditions ['w[11]==2+w[9]', 'w[12]==-5+w[7]']
Scenario [0, 1, 5, 7] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]']
Scenario [0, 1, 2, 7] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]']
Scenario [0, 1, 7] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]']
Scenario [0, 1, 2, 5] with 10 appends and conditions ['w[7]==2+w[5]', 'w[11]==2+w[9]', 'w[12]==-3+w[5]']
Scenario [0, 1, 5] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[11]==2+w[9]', 'w[12]==-3+w[5]']
Scenario [0, 1, 2] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[11]==2+w[9]', 'w[12]==-4+w[2]']
Scenario [0, 1, 2, 5] with 10 appends and conditions ['w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-3+w[5]']
Scenario [0, 1, 5] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-3+w[5]']
Scenario [0, 1, 2] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-4+w[2]']
Scenario [0, 1] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==8+w[1]']
Scenario [0, 1, 2] with 9 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]', 'w[12]==-4+w[2]']
Scenario [0, 1] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]', 'w[12]==8+w[1]']
Scenario [0, 1] with 8 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[11]==-1+w[2]', 'w[12]==8+w[1]']

After step i=13: 112 scenarios (could pop)
Scenario [0, 1, 2, 5, 7, 9, 13] with 14 appends and conditions []
Scenario [0, 1, 5, 7, 9, 13] with 13 appends and conditions ['w[4]==-4+w[2]']
Scenario [0, 1, 2, 7, 9, 13] with 13 appends and conditions ['w[5]==-6+w[2]']
Scenario [0, 1, 7, 9, 13] with 12 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]']
Scenario [0, 1, 2, 5, 9, 13] with 13 appends and conditions ['w[7]==2+w[5]']
Scenario [0, 1, 5, 9, 13] with 12 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]']
Scenario [0, 1, 2, 9, 13] with 12 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]']
Scenario [0, 1, 2, 5, 7, 13] with 13 appends and conditions ['w[9]==-1+w[7]']
Scenario [0, 1, 5, 7, 13] with 12 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 7, 13] with 12 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]']
Scenario [0, 1, 7, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]']
Scenario [0, 1, 2, 5, 13] with 12 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 5, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]']
Scenario [0, 1, 2, 5, 7, 13] with 13 appends and conditions ['w[11]==2+w[9]']
Scenario [0, 1, 5, 7, 13] with 12 appends and conditions ['w[4]==-4+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 7, 13] with 12 appends and conditions ['w[5]==-6+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 7, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 5, 13] with 12 appends and conditions ['w[7]==2+w[5]', 'w[11]==2+w[9]']
Scenario [0, 1, 5, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[11]==2+w[9]']
Scenario [0, 1, 2, 5, 13] with 12 appends and conditions ['w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 5, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[11]==-1+w[2]']
Scenario [0, 1, 2, 5, 7, 13] with 13 appends and conditions ['w[12]==-1+w[9]']
Scenario [0, 1, 5, 7, 13] with 12 appends and conditions ['w[4]==-4+w[2]', 'w[12]==-1+w[9]']
Scenario [0, 1, 2, 7, 13] with 12 appends and conditions ['w[5]==-6+w[2]', 'w[12]==-1+w[9]']
Scenario [0, 1, 7, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[12]==-1+w[9]']
Scenario [0, 1, 2, 5, 13] with 12 appends and conditions ['w[7]==2+w[5]', 'w[12]==-1+w[9]']
Scenario [0, 1, 5, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[12]==-1+w[9]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[12]==-1+w[9]']
Scenario [0, 1, 2, 5, 13] with 12 appends and conditions ['w[9]==-1+w[7]', 'w[12]==-5+w[7]']
Scenario [0, 1, 5, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[12]==-3+w[5]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[12]==-3+w[5]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[12]==-4+w[2]']
Scenario [0, 1, 2, 5, 13] with 12 appends and conditions ['w[11]==2+w[9]', 'w[12]==-5+w[7]']
Scenario [0, 1, 5, 13] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[7]==2+w[5]', 'w[11]==2+w[9]', 'w[12]==-3+w[5]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[11]==2+w[9]', 'w[12]==-3+w[5]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[11]==2+w[9]', 'w[12]==-4+w[2]']
Scenario [0, 1, 2, 13] with 11 appends and conditions ['w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-3+w[5]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-3+w[5]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-4+w[2]']
Scenario [0, 13] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==8+w[1]']
Scenario [0, 1, 13] with 10 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]', 'w[12]==-4+w[2]']
Scenario [0, 13] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]', 'w[12]==8+w[1]']
Scenario [0, 13] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[11]==-1+w[2]', 'w[12]==8+w[1]']
Scenario [0, 1, 2, 5, 7, 9] with 13 appends and conditions ['w[13]==-4+w[9]']
Scenario [0, 1, 5, 7, 9] with 12 appends and conditions ['w[4]==-4+w[2]', 'w[13]==-4+w[9]']
Scenario [0, 1, 2, 7, 9] with 12 appends and conditions ['w[5]==-6+w[2]', 'w[13]==-4+w[9]']
Scenario [0, 1, 7, 9] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[13]==-4+w[9]']
Scenario [0, 1, 2, 5, 9] with 12 appends and conditions ['w[7]==2+w[5]', 'w[13]==-4+w[9]']
Scenario [0, 1, 5, 9] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[13]==-4+w[9]']
Scenario [0, 1, 2, 9] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[13]==-4+w[9]']
Scenario [0, 1, 2, 5, 7] with 12 appends and conditions ['w[9]==-1+w[7]', 'w[13]==-8+w[7]']
Scenario [0, 1, 5, 7] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[13]==-8+w[7]']
Scenario [0, 1, 2, 7] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[13]==-8+w[7]']
Scenario [0, 1, 7] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[13]==-8+w[7]']
Scenario [0, 1, 2, 5] with 11 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[13]==-6+w[5]']
Scenario [0, 1, 5] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[13]==-6+w[5]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[13]==-7+w[2]']
Scenario [0, 1, 2, 5, 7] with 12 appends and conditions ['w[11]==2+w[9]', 'w[13]==-8+w[7]']
Scenario [0, 1, 5, 7] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[11]==2+w[9]', 'w[13]==-8+w[7]']
Scenario [0, 1, 2, 7] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[11]==2+w[9]', 'w[13]==-8+w[7]']
Scenario [0, 1, 7] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[11]==2+w[9]', 'w[13]==-8+w[7]']
Scenario [0, 1, 2, 5] with 11 appends and conditions ['w[7]==2+w[5]', 'w[11]==2+w[9]', 'w[13]==-6+w[5]']
Scenario [0, 1, 5] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[11]==2+w[9]', 'w[13]==-6+w[5]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[11]==2+w[9]', 'w[13]==-7+w[2]']
Scenario [0, 1, 2, 5] with 11 appends and conditions ['w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[13]==-6+w[5]']
Scenario [0, 1, 5] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[13]==-6+w[5]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[13]==-7+w[2]']
Scenario [0, 1] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[13]==5+w[1]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]', 'w[13]==-7+w[2]']
Scenario [0, 1] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]', 'w[13]==5+w[1]']
Scenario [0, 1] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[11]==-1+w[2]', 'w[13]==5+w[1]']
Scenario [0, 1, 2, 5, 7] with 12 appends and conditions ['w[12]==-1+w[9]', 'w[13]==-8+w[7]']
Scenario [0, 1, 5, 7] with 11 appends and conditions ['w[4]==-4+w[2]', 'w[12]==-1+w[9]', 'w[13]==-8+w[7]']
Scenario [0, 1, 2, 7] with 11 appends and conditions ['w[5]==-6+w[2]', 'w[12]==-1+w[9]', 'w[13]==-8+w[7]']
Scenario [0, 1, 7] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[12]==-1+w[9]', 'w[13]==-8+w[7]']
Scenario [0, 1, 2, 5] with 11 appends and conditions ['w[7]==2+w[5]', 'w[12]==-1+w[9]', 'w[13]==-6+w[5]']
Scenario [0, 1, 5] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[12]==-1+w[9]', 'w[13]==-6+w[5]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[12]==-1+w[9]', 'w[13]==-7+w[2]']
Scenario [0, 1, 2, 5] with 11 appends and conditions ['w[9]==-1+w[7]', 'w[12]==-5+w[7]', 'w[13]==-6+w[5]']
Scenario [0, 1, 5] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]', 'w[13]==-6+w[5]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]', 'w[13]==-7+w[2]']
Scenario [0, 1] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[12]==-5+w[7]', 'w[13]==5+w[1]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[12]==-3+w[5]', 'w[13]==-7+w[2]']
Scenario [0, 1] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[12]==-3+w[5]', 'w[13]==5+w[1]']
Scenario [0, 1] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[12]==-4+w[2]', 'w[13]==5+w[1]']
Scenario [0, 1, 2, 5] with 11 appends and conditions ['w[11]==2+w[9]', 'w[12]==-5+w[7]', 'w[13]==-6+w[5]']
Scenario [0, 1, 5] with 10 appends and conditions ['w[4]==-4+w[2]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]', 'w[13]==-6+w[5]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[5]==-6+w[2]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]', 'w[13]==-7+w[2]']
Scenario [0, 1] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[11]==2+w[9]', 'w[12]==-5+w[7]', 'w[13]==5+w[1]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[7]==2+w[5]', 'w[11]==2+w[9]', 'w[12]==-3+w[5]', 'w[13]==-7+w[2]']
Scenario [0, 1] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[11]==2+w[9]', 'w[12]==-3+w[5]', 'w[13]==5+w[1]']
Scenario [0, 1] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[11]==2+w[9]', 'w[12]==-4+w[2]', 'w[13]==5+w[1]']
Scenario [0, 1, 2] with 10 appends and conditions ['w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-3+w[5]', 'w[13]==-7+w[2]']
Scenario [0, 1] with 9 appends and conditions ['w[4]==-4+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-3+w[5]', 'w[13]==5+w[1]']
Scenario [0, 1] with 9 appends and conditions ['w[5]==-6+w[2]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==-4+w[2]', 'w[13]==5+w[1]']
Scenario [0] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[5]==6+w[1]', 'w[9]==-1+w[7]', 'w[11]==-2+w[7]', 'w[12]==8+w[1]', 'w[13]==4+w[0]']
Scenario [0, 1] with 9 appends and conditions ['w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]', 'w[12]==-4+w[2]', 'w[13]==5+w[1]']
Scenario [0] with 8 appends and conditions ['w[4]==-4+w[2]', 'w[7]==2+w[5]', 'w[9]==1+w[5]', 'w[11]==0+w[5]', 'w[12]==8+w[1]', 'w[13]==4+w[0]']
Scenario [0] with 8 appends and conditions ['w[5]==-6+w[2]', 'w[7]==1+w[2]', 'w[9]==0+w[2]', 'w[11]==-1+w[2]', 'w[12]==8+w[1]', 'w[13]==4+w[0]']
