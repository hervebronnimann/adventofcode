n = list(open("input.txt").read().strip())
m = len(n)//2

print(sum([ int(x) for x,y in zip(n,n[m:]+n[0:m]) if x == y]))
