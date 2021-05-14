def make_adjlist(vertices, edges):
    """
    Args:
        vertices (List(int)): vertices of the graph
        edges (List(tuple(int, int))): edges of the graph

    Returns:
        dict(int, List(int)): Adjacency list of thr graph
    """
    adjlist = dict(zip(vertices, [[] for vertex in vertices]))
    for u, v in edges:
        adjlist[u].append(v)
    return adjlist

class Graph():
    def __init__(self, vertices, edges, weights = None):
        self.v = vertices
        self.e = edges
        self.weights = weights
        self.adjlist = make_adjlist(vertices, edges)
        
    from ._breadth_first_traversal import breadth_first_search, unweighted_shortest_paths, bfs_tree, is_bipartite 
    
    from ._depth_first_traversal import depth_first_search
    
    from ._shortest_paths import find_shortest_paths, find_shortest_paths, find_shortest_paths