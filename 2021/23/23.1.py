from collections import defaultdict
from copy import deepcopy
import heapq as heap

# Hallway: 1,2,4,6,8,10,11  (distances easy to compute)
# Top cell: 13,15,17,19
# Bottom cell: 23,25,27,29
# Tricks with arithmetic

def hboard(board):
  ''' Encode a board (map of positions) into an array for hashing and putting into sets. '''
  return tuple([board[i] if i in board.keys() else 0 for i in range(0,32)])

hall =  { 1, 2, 4, 6, 8, 10, 11 }          # keys for hall positions
topdest = { 13, 15, 17, 19 }               # keys for cells
edest = { 1:13, 10:15, 100:17, 1000:19 }   # final destination for each piece

def print_board(prefix,b,cost):
  c = { 0:'.', 1:'A', 10:'B', 100:'C', 1000:'D' }
  print('%s#############' % prefix)
  print('%s#%s%s.%s.%s.%s.%s%s#' % (prefix,c[b[1]],c[b[2]],c[b[4]],c[b[6]],c[b[8]],c[b[10]],c[b[11]]))
  print('%s###%s#%s#%s#%s###' % (prefix,c[b[13]],c[b[15]],c[b[17]],c[b[19]]))
  print('%s  #%s#%s#%s#%s#  ' % (prefix,c[b[23]],c[b[25]],c[b[27]],c[b[29]]))
  print('%s  #########  ' % prefix)
  print('%s  Cost so far: %d' % (prefix,cost))

iboard = hboard({
  1:0, 2:0, 4:0, 6:0, 8:0, 10:0, 11:0,
  # 13:10, 15:100,  17:10,  19:1000,  # For the example
  # 23:1,  25:1000, 27:100, 29:1
  13:1000, 15:1,   17:1,  19:1000,    # For my input
  23:100,  25:100, 27:10, 29:10
})

eboard = hboard({
  1:0, 2:0, 4:0, 6:0, 8:0, 10:0, 11:0,
  13:1, 15:10, 17:100, 19:1000,
  23:1, 25:10, 27:100, 29:1000
})

def neighbors(board):
  ''' Compute all the possible moves from a given board. '''
  for h in hall:
    ''' Boarding a hallway piece to its destination '''
    if board[h]==0: continue  # empty hallway cell
    d = edest[board[h]]; occupied = False
    if board[d]!=0: continue # destination is occupied
    if board[d+10]!=0 and board[d+10]!=board[h]: continue # bottom is occupied by misplaced piece
    if h<d-10:
      for h2 in range(h+1,d-10):
        if h2 in hall and board[h2]!=0: occupied=True; break
    else:
      for h2 in range(d-9,h):
        if h2 in hall and board[h2]!=0: occupied=True; break
    if occupied: continue
    cost = abs(d-10-h)+1 # horizontal plus one move down
    if board[d+10]==0: d += 10; cost += 1   # slide into bottom of cell
    b2=list(board); b2[d]=b2[h]; b2[h]=0
    # print("Found move for %d from hallway %d to dest %d (cost %d)" % (b2[d], h, d, cost*b2[d]))
    yield tuple(b2),cost*b2[d]
  for d in topdest:
    ''' Moving a piece to the hallway. '''
    d2=d; cost = 1  # for the move up
    if board[d]==0:
      d += 10; cost += 1
      if board[d]==0: continue # boths cells empty, go to next destination
      if edest[board[d]]==d2: continue  # already in its place
    else:
      if edest[board[d]]==d2 and edest[board[d+10]]==d2 : continue  # cell is in place (both top and bottom)
    for h in range(d2-10,0,-1):
      if h not in hall: continue
      if board[h]!=0: break
      b2=list(board); b2[h]=b2[d]; b2[d]=0;
      # print("Found move for %d from dest %d to hallway %d (cost %d)" % (b2[h], d, h, (cost+abs(d-10-h))*b2[h]))
      yield tuple(b2), (cost+abs(d2-10-h))*b2[h]
    for h in range(d2-10,12):
      if h not in hall: continue
      if board[h]!=0: break
      b2=list(board); b2[h]=b2[d]; b2[d]=0;
      # print("Found move for %d from dest %d to hallway %d (cost %d)" % (b2[h], d, h, (cost+abs(h-d-10))*b2[h]))
      yield tuple(b2), (cost+abs(h-d2+10))*b2[h]

print_board("Start: ",iboard,0)
print_board("Dest:  ",eboard,0)

# Now that we can compute the neighbors of a board, run a Disjktra until visiting eboard
dist={}
visited=set()
pq=[]
heap.heappush(pq,(0,iboard))
while pq:
  c,board = heap.heappop(pq)
  visited.add(board)
  # print_board('',board,c)
  if board==eboard: 
    print('Minimum: %d' % c); break
  for n,cost in neighbors(board):
    if n in visited: continue
    newdist = c+cost
    # print_board('    ---> ',n,c+cost)
    if n not in dist.keys() or newdist < dist[n]:
      dist[n] = newdist
      heap.heappush(pq,(newdist,n))
