def score(t):

with open("input.txt",'r') as f:
  m = dict()  # number of winning numbers for each card
  for s in f:
    s = s.strip().split(":")
    t = s[1].strip().split("|")
    win_cards = set(t[0].split())
    my_cards = set(t[1].split())
    m[id] = len(win_cards.intersection(my_cards))
  # print(m)
  n = dict([ (i,1) for i in m])  # number of copies of each card
  for i in range(1,len(m)+1):
    # print(f"Card {i} with {m[1]} winning numbers adding {n[i]} copies of cards {[j for j in range(i+1,min(i+1+m[i],len(m)+1))]}")
    for j in range(i+1,min(i+1+m[i],len(m)+1)):
      n[j] += n[i] 
  print(n)

print(sum(n.values()))
