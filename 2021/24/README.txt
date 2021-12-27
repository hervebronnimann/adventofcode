Rewritten the input looks like (from left to right, one column at a time):

    COL 1     COL 2     COL 3     COL 4     COL 5     COL 6     COL 7     COL 8     COL 9     COL 10    COL 11    COL 12    COL 13    COL 14
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
      ztop = 0 if len(z)==0 else z[-1]
      if c5[i]==26: z.pop() // pop happens exactly 7 times out of 14
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
      j=-1 if len(sc.z)==0 else sc.z[-1]
      if len(sc.z)>0 and c5[i]==26: sc.z.pop()
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

And after correcting the mistake (I had the pop before capturing j, in a previous analysis! drove me crazy!)
now I get the following output:

Scenario [] with 7 appends and conditions ['w[4]==w[3]+6', 'w[5]==w[2]-6', 'w[7]==w[6]-2', 'w[9]==w[8]-1', 'w[11]==w[10]+0', 'w[12]==w[1]+8', 'w[13]==w[0]+4']

Which means
* w[3] must be <=3 (otherwise no solution for w[4]), and max is w[3]==3 then w[4]=9.
* w[5] must be <=3 (because w[2]<=9), and max w[5]==3 then w[2]=9.
* w[7] must be <=7 , and max is w[7]==7 then w[6]=9
* w[9] must be <=8 , and max is w[9]==8 then w[8]=9
* w[11]==w[10] and both could be up to 9
* w[12]==9 and w[1]==1
* w[0] must be <=5 (otherwise no solution for w[13]), and max is w[0]==5 then w[13]==9.

Overall, the maximum solution is w=[5,1,9,3,9,3,9,7,9,8,9,9,9,9] or 51939397989999.
And the minumum solution (for part 2) is [1,1,7,1,7,1,3,1,2,1,1,1,9,5] or 11717131211195.
