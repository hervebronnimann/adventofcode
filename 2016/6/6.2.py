from collections import Counter

input = open("input.txt",'r').read().strip().split('\n')

res = ''
for i in range(len(input[0])):
    res += Counter([x[i] for x in input]).most_common()[-1][0]
print(res)
