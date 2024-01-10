import itertools

regs = ['a','b','c','d']

def run(state:dict):
    L,i,n = [],0,0
    while i < len(input):
        cmd = input[i].strip().split()
        if cmd[0]=='tgl':
            n = state[cmd[1]] if cmd[1] in regs else int(cmd[1])
            print(i,cmd)
            if i+n < len(input):
                cmd = input[i+n].strip().split()
                cmd[0] = {'inc':'dec','dec':'inc','tgl':'inc','out':'inc','jnz':'cpy','cpy':'jnz'}[cmd[0]]
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
        elif cmd[0]=='out':
            val = state[cmd[1]] if cmd[1] in regs else int(cmd[1])
            if val != n%2: return False
            n += 1
            if n>10000: return True
        elif cmd[0]=='inc':
            if cmd[1] in regs:
                state[cmd[1]] += 1
        elif cmd[0]=='dec':
            if cmd[1] in regs:
                state[cmd[1]] -= 1
        #print(i,cmd,state)
        i += 1
    return L

for x in itertools.count(1):
    print("Trying ",x);
    input = open("input.txt",'r').read().strip().split('\n')
    state = { x:0 for x in regs }
    state['a'] = x
    if run(state):
        print("Found ",x); exit(0)
