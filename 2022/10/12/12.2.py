from collections import defaultdict

def height(x):
  if x == 'S': return 0
  if x == 'E': return 25
  return ord(x[0])-ord('a')
  
grid=[list(map(height,l)) for l in """
abcccccccccaaaaaaaaaaccccccccccccaaaaaaaaccaaccccccccccccccccccccccccccccccccccccccccccccaaaaaa
abccccccccccaaaaaaaaaccccccccccccaaaaaaaaaaaacccccccccccaacccacccccccccccccccccccccccccccaaaaaa
abcccccccccccaaaaaaacccccccccccccaaaaaaaaaaaaaacccccccccaaacaacccccccccaaaccccccccccccccccaaaaa
abccccccccccaaaaaaccccccccccccccaaaaaaaaaaaaaaaccccccccccaaaaaccccccccccaaacccccccccccccccccaaa
abccccccccccaaaaaaaccccccccccccaaaaaaaaaaaaaacccccccccccaaaaaacccccccccaaaacccccccccccccccccaac
abaaccaaccccaaccaaaccccccccaaaaaaaaaaaaaaacaaccccccccccaaaaaaaacccccccccaaalcccccccccccccccaaac
abaaaaaacccccccccaaccccccccaaaaaacccaaaacccaaccccccccccaaaaaaaaccccccccalllllllcccccccccccccccc
abaaaaaacccccccaaacccccccccaaaaccccccaaaccccaaaaacccccccccaacccccccaaaakllllllllcccccccaacccccc
abaaaaaacccccccaaaacccccccccaacccccccaaaccccaaaaacccccccccaacccccccaakkklllpllllccccacaaacccccc
abaaaaaaaccccccaaaaccccaaccccccccccccccccccaaaaaaccccccccccccccccccckkkkpppppplllcccaaaaaaacccc
abaaaaaaacaaaccaaaaccaaaaaaccccccccccccccccaaaaaacccccccaaaccccckkkkkkkpppppppplllcddaaaaaacccc
abcaaaacccaacccccccccaaaaaacccccaaaccccccccaaaaaacccccccaaaaccjkkkkkkkpppppuppplmmdddddaaaccccc
abccaaaaaaaaaccccccccaaaaaaccccaaaaaacccccccaaacccccccccaaaajjjkkkkkrpppuuuuupppmmmdddddacccccc
abccccaaaaaaaacccccccaaaaacccccaaaaaacccccccccccccccccccaaacjjjjrrrrrrppuuuuupqqmmmmmddddaccccc
abccccaaaaaaaaacccccccaaaacccccaaaaaaccccccccccccccccccccccjjjrrrrrrrrpuuuxuvvqqqmmmmmddddccccc
abccccaaaaaaaaacccccccccccccccccaaaaaccccaacccaccccccccaaccjjjrrrruuuuuuuxxyvvqqqqqmmmmmdddcccc
abccccaaaaaaaacccccccccaaaccccccaacaaccccaaacaacccaaacaaaccjjjrrrtuuuuuuuxxyvvvqqqqqmmmmdddcccc
abccaaaaaaaacccccccccccaaaaaccccccccccccccaaaaacccaaaaaaaccjjjrrttttxxxxxxyyvvvvvqqqqmmmmdeeccc
abccaaaccaaaccccccccaacaaaaacccccccccccccaaaaaacccaaaaaacccjjjrrtttxxxxxxxyyvvvvvvvqqqmmmeeeccc
abaaaaaaaaaacccaaaccaaaaaaaaaaaccaaaccccaaaaaaaacccaaaaaaaajjjqqrttxxxxxxxyyyyyyvvvqqqnnneeeccc
SbaaaaaaaaccccaaaaccaaaaaaaaaaaaaaaaacccaaaaaaaaccaaaaaaaaacjjjqqtttxxxxEzzyyyyvvvvqqqnnneeeccc
abcaaaaaacccccaaaaccccaaaaaaaccaaaaaaccccccaaccccaaaaaaaaaaciiiqqqtttxxxyyyyyyvvvvrrrnnneeecccc
abcaaaaaacccccaaaacccaaaaaaaaccaaaaaaccccccaaccccaaacaaacccciiiqqqqttxxyyyyyywvvvrrrnnneeeecccc
abcaaaaaaccccccccccccaaaaaaaaacaaaaacccccccccccccccccaaaccccciiiqqtttxxyyyyyywwrrrrnnnneeeccccc
abcaaacaacccccaacccccaaaaaaaaacaaaaacccccccccccccccccaaaccccciiiqqttxxxywwyyywwrrrnnnneeecccccc
abccccccccaaacaaccccccccccacccccccccccccccccccccccccccccccccciiqqqttxxwwwwwwywwrrrnnneeeccccccc
abccaacccccaaaaaccccccccccccccccccccccccccccccccccccccccaacaaiiqqqttwwwwsswwwwwrrrnnfffeccccccc
abaaaaccccccaaaaaacccccccccccccccccccccccccccccaaaccccccaaaaaiiqqqttssssssswwwwrrronfffaccccccc
abaaaaaacccaaaaaaacccccccccccccccccccccccccccaaaaaacccccaaaaaiiqqqssssssssssswrrrooofffaaaacccc
abaaaaaaccaaaaaacccccccccccccccccccccccccccccaaaaaacccccaaaaaiiqqqppssspppssssrrrooofffaaaacccc
abaaaaaaccaacaaacccccccccccccccccccccccccccccaaaaaacccccaaaaaiihpppppppppppossrrooofffaaaaacccc
abaaaaccccccccaacccccccccccccccccccccccccccccaaaaaccccccccaaahhhhppppppppppoooooooofffaaaaccccc
abaaaaccccccccccaacccccccccccccccccaaacccccccaaaaacccccccccccchhhhhhhhhhggpoooooooffffaaaaccccc
abccaacccccccacaaaccccccccccccccccaaaaacccccccccccccccccccccccchhhhhhhhhggggoooooffffaacaaacccc
abccccccccccaaaaacaaccccccccccccccaaaaaccccccccccccccccccccccccchhhhhhhhggggggggggffcaacccccccc
abccccccccccaaaaaaaaccccccccccccccaaaacccaacccccccccccaccccccccccccccaaaaaggggggggfcccccccccccc
abccccccccccccaaaaaccccaacccccccccaaaacaaaaccccccccaaaaccccccccccccccaaaacaaagggggcccccccccaccc
abcccccccccccaaaaacccccaacccccccccaaaaaaaaaccccccccaaaaaaccccccccccccaaaccaaaacccccccccccccaaac
abcccccccccccaacaaccaaaaaaaacccaaaaaaaaaaaccccccccccaaaaccccccccccccccaccccaaacccccccccccccaaaa
abccccccccccccccaaccaaaaaaaaccaaaaaaaaaaaccccccccccaaaaacccccccccccccccccccccacccccccccccccaaaa
abccccccccccccccccccccaaaaacccaaaaaaaaaaaacccccccccaacaacccccccccccccccccccccccccccccccccaaaaaa
""".strip().split('\n')]

print(grid)
# S=(20,0)
E=(20,72)
# E=(2,5)

N = len(grid)
M = len(grid[0])
INF = 9999999999

def dijkstra(S):
  flood = [[INF for j in range(M)] for i in range(N)]
  flood[S[0]][S[1]] = 0
  iters=0
  q=[S]
  while flood[E[0]][E[1]]==INF:
    iters += 1
    q1 = []
    if len(q) == 0: return INF
    for i,j in q:
      for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if i+dy<0 or i+dy>=N: continue
        if j+dx<0 or j+dx>=M: continue
        if flood[i+dy][j+dx]==INF and grid[i+dy][j+dx] <= 1 + grid[i][j]:
          flood[i+dy][j+dx] = flood[i][j]+1
          q1.append((i+dy,j+dx))
    q = q1
  return iters

Ss = []
for i in range(N):
  for j in range(M):
    if grid[i][j]==0: Ss.append((i,j))

print(min([dijkstra(S) for S in Ss]))
