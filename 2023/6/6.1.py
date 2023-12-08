#example
time = [ int(k) for k in "7  15   30".split()]
dist = [ int(k) for k in "9  40  200".split()]
print(time, dist)

#input
time = [ int(k) for k in "54708275".split()]
dist = [ int(k) for k in "239114212951253".split()]
print(time, dist)

res = 1
for i in range(len(time)):
  res *= sum([j*(time[i]-j) > dist[i] for j in range(1,time[i]+1)])
print(res)
