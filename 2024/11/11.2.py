import functools

input=[int(x) for x in "6 11 33023 4134 564 0 8922422 688775".split()]

@functools.cache
def solve(x,n):
    if n==0: return 1
    if x==0:
        return solve(1,n-1)
    xx = str(x)
    if len(xx)%2 == 0:
        r = len(xx)//2
        return solve(int(xx[0:r]), n-1) + solve(int(xx[r:]), n-1)
    return solve(x * 2024,n-1)

print(sum([solve(x,25) for x in input]))
print(sum([solve(x,75) for x in input]))
