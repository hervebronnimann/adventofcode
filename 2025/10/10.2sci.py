import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def ints(l): return [ int(x) for x in l.split(',') ]

def solve(joltage,buttons):
    """ Maximize sum(x) such that x>=0, sum(x[j]*buttons[j][i] for j in range(m)) == joltage[i] for each i in range(n). """
    # scipy works with minimize so we make -sum(x), also transpose buttons to fit scipy
    n,m = len(joltage),len(buttons)
    buttons = [ [buttons[j][i] for j in range(m)] for i in range(n) ]

    # Example problem: Minimize c^T * x subject to A * x <= b_u and x >= 0, with all x as integers.
    c = np.array([1]*m) # Objective: maximize sum(x), aka minimize -sum(x)
    A = np.array(buttons) # Constraint matrix
    b_u = np.array(joltage) # Upper bounds for constraints (<=)
    b_l = np.array([-np.inf]*n) # Upper bounds for constraints (<=)

    # Create LinearConstraint object
    constraints = LinearConstraint(A, b_u, b_u)

    # Specify integrality constraints (1 for integer, 0 for continuous)
    integrality = np.ones_like(c) # All variables must be integers

    return int(milp(c=c, constraints=constraints, integrality=integrality).fun + 0.001)

sol = 0
for l in open('input.txt','r'):
    x=l.strip().split(' ')
    pattern,buttons,joltage = x[0],x[1:-1],x[-1]
    pattern = pattern[1:-1]
    buttons = [ set(ints(x[1:-1])) for x in buttons ]
    buttons = [ [1 if i in bb else 0 for i in range(len(pattern))] for bb in buttons ]
    joltage = ints(joltage[1:-1])
    sol += solve(joltage,buttons)
print(sol)
