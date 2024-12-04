import re

text = ''
with open("input.txt", 'r') as f:
    text = f.read()

pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
enable = True
n = 0
for x in re.findall(pattern, text):
    if x == "do()": enable = True
    elif x == "don't()": enable = False
    elif enable:
        print(x, enable)
        x = x[4:-1].split(',')
        n = n + int(x[0]) * int(x[1])
print(n)
