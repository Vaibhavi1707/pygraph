def dfs_visit(self, u, color, predecessor, topo_order):
    color[u] = "gray"
    
    for v in self.adjlist[u]:
        if color[v] == "white":
            predecessor[v] = u
            self.dfs_visit(v, color, predecessor, topo_order)    
    
    color[u] = "black"
    topo_order.insert(0, u)

def depth_first_search(self):
    """
    Runs DFS
    Args:
        src (int, optional): Source vertex from where DFS is to be performed. 
                            Defaults to None.
    
    Returns: discovery_times, finish_times, parents 
        predecessor List[int], topo_order List[int]: List of dfs predecessors such that 
                    predecessor[i] = predecessor of i found during DFS traversal and 
                    topo sort of the graph obtained.
    """
    color = ["white"] * len(self.v)
    predecessor = [None] * len(self.v)
    topo_order = []
    
    for vertex in self.v:
        if color[vertex] == "white":
            self.dfs_visit(vertex, color, predecessor, topo_order)
            
    return predecessor, topo_order
            
def topological_sort(self):
    """
    Returns:
        List(int): Topological sort of vertices of a graph.
    """
    topo_order = self.depth_first_search()[1]
    
    position = [-1] * len(self.v)
    
    for i, v in enumerate(topo_order):
        position[v] = i
        
    for u, v in self.e:
        if position[u] > position[v]:
            return None
        
    return topo_order 

def is_cyclic(self):
    return not self.topological_sort()   