# If you want to use the Graph constructor anywhere in your code.
import math, sys
# sys.path.insert(1, "../../../")
# import pygraph.src.Graph

def find_shortest_paths(self, s):
    """
    Returns the shortest distance from a source s to all other vertices 
        in a weighted graph.
    Uses Bellman Ford algorithm.
    Args:
        s (int): Source vertex from which shortest path lengths to all other 
                reachable vertices is to be found.
                
    Returns:
        dist (List(int)), pre (List(int)): Shortest path lengths between source s to all other 
                vertices of a weighted graph and predecessor in the path from s to each vertex 
                respectively.
    """
    #intialize distance and predecessor
    dist, pre = [math.inf for vertex in self.v], [None for vertex in self.v]
    for vertex in self.v:
        dist[vertex], pre[vertex] = float('inf'), None
    dist[s] = 0 

    #Relax the edges
    for i in range(len(self.v) - 1):
        for vertex in self.v:
            for adj_vertex in self.adjlist[vertex]:
                if dist[adj_vertex] > dist[vertex] + self.weights[vertex][adj_vertex]:
                    dist[adj_vertex], pre[adj_vertex] = dist[vertex] + self.weights[vertex][adj_vertex], vertex
    
    #check for negative cycles
    for vertex in self.v:
        for adj_vertex in self.adjlist[vertex]:
            if dist[adj_vertex] > dist[vertex] + self.weights[vertex][adj_vertex]:
                return None
 
    return dist, pre
