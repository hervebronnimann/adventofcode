from collections import defaultdict

edges = defaultdict(list)
invedges = defaultdict(list)
for l in open('input.txt','r'):
    x,e = l.strip().split(':')
    edges[x] = e.strip().split()
    for y in edges[x]:
        invedges[y].append(x)

def topological_sort_dfs(graph):
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
    dfs_visit('you')

    # The order needs to be reversed
    return stack[::-1]

n = defaultdict(int)
n['you'] = 1
for y in topological_sort_dfs(edges)[1:]:
    n[y] = sum([n[x] for x in invedges[y]])
print(n)
print(n['out'])
