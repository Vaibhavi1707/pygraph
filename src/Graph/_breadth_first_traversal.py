import pygraph.src.Graph as Graph
import math

def breadth_first_search(self, src_vertex = 0):
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
    return self.breadth_first_search(src_vertex)[0]

def bfs_tree(self, src_vertex = 0):
    edges, vertices = [], [src_vertex]
    parents = self.breadth_first_search(src_vertex)[1]
    
    for u, parent in enumerate(parents):
        if parent != None:
            edges.append((parent, u))
            vertices.append(u)
            
    return Graph(vertices, edges)
        
def is_bipartite(self, src_vertex = 0):
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