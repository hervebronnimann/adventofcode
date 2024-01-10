regs = ['a','b','c','d']

def run(state:dict):
    i = 0
    while i < len(input):
        cmd = input[i].strip().split()
        if cmd[0]=='tgl':
            n = state[cmd[1]] if cmd[1] in regs else int(cmd[1])
            print(i,cmd)
            if i+n < len(input):
                cmd = input[i+n].strip().split()
                cmd[0] = {'inc':'dec','dec':'inc','tgl':'inc','jnz':'cpy','cpy':'jnz'}[cmd[0]]
                input[i+n] = ' '.join(cmd)
                print("Toggled: ",i+n, input[i+n])
            i += 1
            continue
        if cmd[0]=='jnz':
            cond = state[cmd[1]] if cmd[1] in regs else int(cmd[1])
            if i==15: print(i,cmd,state)
            if cond:
                i += state[cmd[2]] if cmd[2] in regs else int(cmd[2])
                continue
        elif cmd[0]=='cpy':
            if cmd[2] in regs:
                state[cmd[2]] = state[cmd[1]] if cmd[1] in regs else int(cmd[1])
        elif cmd[0]=='inc':
            if cmd[1] in regs:
                state[cmd[1]] += 1
        elif cmd[0]=='dec':
            if cmd[1] in regs:
                state[cmd[1]] -= 1
        #print(i,cmd,state)
        i += 1
    return state['a']

input = open("input.txt",'r').read().strip().split('\n')
state = { x:0 for x in regs }
state['a']=7  # WHY COULD I NOT READ!?
print("Part 1:", run(state))

# Ahah!  We modify input above, so need to read it again!
# input = open("input.txt",'r').read().strip().split('\n')
# state = { x:0 for x in regs }
# state['a']=12
# print("Part 2:", run(state))
# This will never finish, because it is clear what is happening:

# % py 23.1.py | grep -B1 tgl
# 15 ['jnz', 'd', '-2'] {'a': 42, 'b': 5, 'c': 10, 'd': 0}
# 15 ['jnz', 'd', '-2'] {'a': 210, 'b': 4, 'c': 8, 'd': 0}
# 15 ['jnz', 'd', '-2'] {'a': 840, 'b': 3, 'c': 6, 'd': 0}
# 15 ['jnz', 'd', '-2'] {'a': 2520, 'b': 2, 'c': 4, 'd': 0}
# 15 ['jnz', 'd', '-2'] {'a': 5040, 'b': 1, 'c': 2, 'd': 0}
# The rest of simply adding 75*72 to the factorial.

print("Part 2:", 2*3*4*5*6*7*8*9*10*11*12 + 75*72)
