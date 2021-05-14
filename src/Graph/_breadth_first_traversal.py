import math, sys
sys.path.insert(1, "../../../")
import pygraph.src.Graph

def breadth_first_search(self, src_vertex = 0):
    """
    Performs BFS on a graph
    Args:
        src_vertex (int, optional): Source vertex from which breadth first search 
                                    is performed. Defaults to 0.

    Returns:
        tuple(List(int), List(int)): Returns the level of each reachable vertex in 
                                    the BFS tree and parent of each vertex found 
                                    during the traversal.
    """
    frontier_from_src = [math.inf] * len(self.v)
    parent = [None for vertex in self.v]
    color = ["white" for vertex in self.v]
    
    frontier_from_src[src_vertex] = 0
    color[src_vertex] = "gray"
    bfs_queue = [src_vertex]
    
    while bfs_queue:
        u = bfs_queue.pop(0)
        for v in self.adjlist[u]:
            if color[v] == "white":
                color[v] = "grey"
                frontier_from_src[v] = frontier_from_src[u] + 1
                parent[v] = u
                bfs_queue.append(v)
        color[u] = "black"
        
    return frontier_from_src, parent        
                
def unweighted_shortest_paths(self, src_vertex = 0):
    """
    Finds the shortest distance from source to all vertices of an unweighted graph
    or the level of each reachable vertex in the BFS tree.
    Args:
        src_vertex (int, optional): Source from where shortest distnce to each 
                                    reachable vertex is computed. Defaults to 0.

    Returns:
        List(int): shortest distance from src_vertex to each reachable vertex in 
                    the graph
    """
    return self.breadth_first_search(src_vertex)[0]

def bfs_tree(self, src_vertex = 0):
    """
    Finds the predecessor subgraph of the given graph obtained from BFS
    Args:
        src_vertex (int, optional): Source vertex from where BFS is performed. 
                                    Defaults to 0.

    Returns:
        Graph(): predecessor subgraph i.e graph containing all the edges, 
                (parent[u], u) as obtained from BFS
    """
    edges, vertices = [], [src_vertex]
    parents = self.breadth_first_search(src_vertex)[1]
    
    for u, parent in enumerate(parents):
        if parent != None:
            edges.append((parent, u))
            vertices.append(u)
            
    return pygraph.src.Graph.Graph(vertices, edges)
        
def is_bipartite(self, src_vertex = 0):
    """
    Checks whether a graph is bipartite or not.
    Args:
        src_vertex (int, optional): Source vertex from where bipartite-ness of a graph is checked. 
                                    Defaults to 0.

    Returns:
        bool: True if graph is bipartite else False.
    """
    frontier_from_src = [math.inf] * len(self.v)
    parent = [None for vertex in self.v]
    color = ["white" for vertex in self.v]
    partition = [1 for vertex in self.v]
    
    frontier_from_src[src_vertex] = math.inf
    color[0] = "gray"
    bfs_queue = [src_vertex]
    
    while bfs_queue:
        u = bfs_queue.pop(0)
        for v in self.adjlist[u]:
            if color[v] == "white":
                color[v] = "grey"
                partition[v] = not bool(partition[u])
                frontier_from_src[v] = frontier_from_src[u] + 1
                parent[v] = u
                bfs_queue.append(v)
            elif partition[v] == partition[u]:
                return False
        color[u] = "black"
        
    return True