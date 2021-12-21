#Input: 6,2 (minus 1 to do %10 more easily)
player=[5,1]
score=[0,0]

def plus1(d): return d+1 if d<100 else 1
def plus2(d): return d+2 if d<99 else 1 if d==99 else 2

die=0
def dice():
  global die
  while True:
    die = plus1(die)
    yield die

n=0
while True:
  n+=3; d = next(dice())
  player[0]+=(d+next(dice())+next(dice())); player[0]%=10
  score[0]+=player[0]+1
  print("Player 1 plays %d,%d,%d and moves to space %d for a total score of %d" % (d,plus1(d),plus2(d),player[0]+1,score[0]))
  if score[0]>=1000: print(0,n,score[1],n*score[1]); break
  n+=3; d = next(dice())
  player[1]+=(d+next(dice())+next(dice())); player[1]%=10
  score[1]+=player[1]+1
  print("Player 2 plays %d,%d,%d and moves to space %d for a total score of %d" % (d,plus1(d),plus2(d),player[1]+1,score[1]))
  if score[1]>=1000: print(1,n,score[0],n*score[0]); break
