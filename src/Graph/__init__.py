def make_adjlist(vertices, edges):
    adjlist = dict(zip(vertices, [[] for vertex in vertices]))
    for u, v in edges:
        adjlist[u].append(v)
    return adjlist

def make_adjmatrix(vertices, edges, weights):
    adjmatrix = [[0 for vertex in vertices] for vertex in vertices]
    for u, v in edges:
        adjmatrix[u][v] = weights[u][v]
    return adjmatrix

class Graph():
    def __init__(self, vertices, edges, weights = None):
        self.v = vertices
        self.e = edges
        self.weights = weights
        self.adjlist = make_adjlist(vertices, edges, weights)
        self.adjmatrix = make_adjmatrix(edges, weights)
        
    from ._breadth_first_traversal import breadth_first_search, unweighted_shortest_paths, bfs_tree, is_bipartite, is_connected 
        