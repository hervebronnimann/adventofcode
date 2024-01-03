input = open("input.txt",'r').read().strip().split('\n')

regs = ['a','b','c','d']

def run(state:dict):
    i = 0
    while i < len(input):
        cmd = input[i].strip().split()
        if cmd[0]=='jnz':
            cond = state[cmd[1]] if cmd[1] in regs else int(cmd[1])
            if cond:
                i += int(cmd[2])
                continue
        elif cmd[0]=='cpy':
            state[cmd[2]] = state[cmd[1]] if cmd[1] in regs else int(cmd[1])
        elif cmd[0]=='inc':
            state[cmd[1]] += 1
        elif cmd[0]=='dec':
            state[cmd[1]] -= 1
        i += 1
    return state['a']

state = { x:0 for x in regs }
print("Part 1:", run(state))

state = { x:0 for x in regs }
state['c'] = 1
print("Part 2:", run(state))
