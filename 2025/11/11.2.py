from collections import defaultdict

edges = defaultdict(list)
invedges = defaultdict(list)
for l in open('input.txt','r'):
    x,e = l.strip().split(':')
    edges[x] = e.strip().split()
    for y in edges[x]:
        invedges[y].append(x)

def topological_sort_dfs(graph,src):
    visited = set()
    stack = [] # The result will be in reverse order initially

    def dfs_visit(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs_visit(neighbor)
        stack.append(node) # Add to stack only after all dependencies are visited

    # Run DFS on all nodes from 'you' to ensure only reachable components are covered
    dfs_visit(src)

    # The order needs to be reversed
    return stack[::-1]

def npaths(graph,src,dst):
    n = defaultdict(int)
    n[src] = 1
    for y in topological_sort_dfs(edges,src)[1:]:
        n[y] = sum([n[x] for x in invedges[y]])
    return n[dst]

print(npaths(edges,'you','out'))

n01 = npaths(edges,'svr','dac')
n02 = npaths(edges,'svr','fft')
n12 = npaths(edges,'dac','fft')
n21 = npaths(edges,'fft','dac')
n13 = npaths(edges,'dac','out')
n23 = npaths(edges,'fft','out')
print(n01*n12*n23)
print(n02*n21*n13)
