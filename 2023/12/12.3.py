from functools import cache

input = open("input.txt",'r').read().strip().split('\n')

@cache
def solve(ln:str, nums:tuple):
    if '?' not in ln: return int([len(x) for x in ln.split('.') if x] == list(nums))
    idx = ln.index('?')
    return solve(ln[:idx] + '.' + ln[idx + 1:], nums) + solve(ln[:idx] + '#' + ln[idx + 1:], nums)

ans = 0
for ln in input:
    ln, nums = ln.split()
    ans += solve(ln, tuple([int(x) for x in nums.split(',')]))
print(ans)
