n = list(open("input.txt").read().strip())
print(n)

print(sum([ int(x) for x,y in zip(n,n[1:]+[n[0]]) if x == y]))
