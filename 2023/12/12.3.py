from functools import cache

input = open("input.txt",'r').read().strip().split('\n')

@cache
def solve(ln, nums):
    if '?' not in ln: return int([len(x) for x in ln.split('.') if x] == list(nums))
    idx = ln.index('?')
    return solve(ln[:idx] + '.' + ln[idx + 1:], nums) + solve(ln[:idx] + '#' + ln[idx + 1:], nums)
 
anss = 0
for i, ln in enumerate(input):
    ln, nums = ln.split()
    anss += solve(ln, tuple([int(x) for x in nums.split(',')]))
print(anss)
