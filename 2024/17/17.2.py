input = open('input.txt').read().strip().split('\n')
# input = open('example2.txt').read().strip().split('\n')

def parse_int(txt): return [int(s) for s in txt.replace(',',' ').split() if s.isdigit()]

A = parse_int(input[0])[0]
B = parse_int(input[1])[0]
C = parse_int(input[2])[0]
print(A,B,C)

ops = parse_int(input[4])
print(ops)

def combo(x):
    global A,B,C
    if x < 4: return x
    if x == 4: return A
    if x == 5: return B
    if x == 6: return C
    assert False, "Invalid operand"

def program(x):
    global A,B,C
    A = x
    B = parse_int(input[1])[0]
    C = parse_int(input[2])[0]
    ptr = 0
    output = []
    state = set((A,B,C,ptr,len(output)))
    while ptr < len(ops)-1:
        if (A,B,C,ptr,len(output)) in state:
            print("Infinite loop: ",x)
            return []
        # print(f'Executing {ops[ptr]} with literal {ops[ptr+1]} and combo {combo(ops[ptr+1])}')
        state.add((A,B,C,ptr,len(output)))
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
            output.append(combo(ops[ptr+1]) % 8)
            # if len(ops) == len(output):
            # if len(ops) < len(output) or ops[len(output)-1] != output[-1]:
            #    return output
        elif ops[ptr] == 6: # 'bdv':
            B = A // 2**combo(ops[ptr+1])
        elif ops[ptr] == 7: # 'cdv':
            C = A // 2**combo(ops[ptr+1])
        ptr += 2
    return output

digits = [0 for _ in range(len(ops))]

# Recursive search for digits, generating the next digits.
# The program is actually written as:
#   1. B = A % 8
#   2. B = B ^ 1
#   3. C = A // 2**B
#   4. A = A // 2**3
#   5. B = B ^ 4
#   6. B = B ^ C
#   7. out B % 8
#   8. jnz 0
# Or equivalently:
#   while A:
#     B = (A % 8) ^ 1
#     out (B ^ 5 ^ (A // 2**B)) % 8
#     A //= 8
# This shows it outputs digits one by one based on the least significant digit of A in octal,
# then the next digit in octal, etc.  But because output also depends on (A // 2**B), other
# digits can affect the output, so starting a search from the least significant digit of A is doomed.
# Instead, we guess the digits of A one by one, starting with the *most* significant, based on
# whether the output of the program matches the *last* digits.  Digits guessed so far can't affect
# the portion of the program output (suffix) that matches so far, unless they spill over from (A//2**B).
# I'm going to guess that doesn't happen very often, but I'll allow for two consecutive digits to be affected,
# that's why the range of d below is 64, not 8.  I tried running with 8 first and guess returned None.
# If 64 didn't work either, I probably would convert the loop for d into an infinite one.

def guess_digits_from(i):
    # When the search reaches here, we must have digits == ops.
    if i == len(digits): return digits
    # First digit can't be 0, so we'll start the search at 1.
    for d in range(1 if i == 0 else 0,64):
        digits[i] = d
        num = sum([x * 8**(len(ops)-1-k) for k,x in enumerate(digits)])
        print('Recursing', i, digits[i], digits, oct(num), num)
        output = program(num)
        # The following test can't be output[-i-1] == ops[-i-1], it has to match the whole suffix.
        if output[-i-1:] == ops[-i-1:]:
            if guess_digits_from(i+1):
                return digits
    # If we can't find anything
    return None

print(guess_digits_from(0))
num = sum([x * 8**(len(ops)-1-k) for k,x in enumerate(digits)])
print(program(num))
print(digits, oct(num), num)
