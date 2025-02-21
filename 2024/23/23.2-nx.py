import networkx as nx

nodes = set()
edges = []
for l in open('input.txt').read().strip().split('\n'):
    p,q = l.split('-')
    nodes.add(p)
    nodes.add(q)
    edges.append((p,q))

# Create a graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Finding all maximal cliques
cliques = list(nx.find_cliques(G))
largest_clique = max(cliques, key=len)
print(','.join(sorted(largest_clique)))
