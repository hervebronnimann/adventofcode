#example
time = [ int(k) for k in "71530".split()]
dist = [ int(k) for k in "940200".split()]
print(time, dist)

#input
time = [ int(k) for k in "54708275".split()]
dist = [ int(k) for k in "239114212951253".split()]
print(time, dist)

# TODO: use quadratic formula
for i in range(len(time)):
  n = 0
  for j in range(1,time[i]+1):
    d = j*(time[i]-j);
    if d > dist[i]: n = j; break
  m = 0
  for j in range(time[i],1,-1):
    d = j*(time[i]-j);
    if d > dist[i]: m = j; break
  print(m-n+1)
