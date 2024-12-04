import re

text = ''
with open("input.txt", 'r') as f:
    text = f.read()

pattern = r'mul\(\d+,\d+\)'
prods = [ x[4:-1].split(',') for x in re.findall(pattern, text)]
print(sum([int(x[0])*int(x[1]) for x in prods]))
