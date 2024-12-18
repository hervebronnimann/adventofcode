input = open('input.txt').read().strip().split('\n')
# input = open('example.txt').read().strip().split('\n')

def parse_int(txt): return [int(s) for s in txt.replace(',',' ').split() if s.isdigit()]

A = parse_int(input[0])[0]
B = parse_int(input[1])[0]
C = parse_int(input[2])[0]
print(A,B,C)

ops = parse_int(input[4])
print(ops)

def combo(x):
    if x < 4: return x
    if x == 4: return A
    if x == 5: return B
    if x == 6: return C
    assert False, "Invalid operand"

ptr = 0
output = []
while ptr < len(ops)-1:
    # print(f'Executing {ops[ptr]} with literal {ops[ptr+1]} and combo {combo(ops[ptr+1])}')
    if ops[ptr] == 0: # 'adv':
        A = A // 2**combo(ops[ptr+1])
    elif ops[ptr] == 1: # 'bxl':
        B = B ^ ops[ptr+1]
    elif ops[ptr] == 2: # 'bst':
        B = combo(ops[ptr+1]) % 8
    elif ops[ptr] == 3: # 'jnz':
        if A>0:
            ptr = ops[ptr+1]
            continue
    elif ops[ptr] == 4: # 'bxc':
        B = B ^ C
    elif ops[ptr] == 5: # 'out':
        output.append(str(combo(ops[ptr+1]) % 8))
    elif ops[ptr] == 6: # 'bdv':
        B = A // 2**combo(ops[ptr+1])
    elif ops[ptr] == 7: # 'cdv':
        C = A // 2**combo(ops[ptr+1])
    ptr += 2
print(','.join(output))
