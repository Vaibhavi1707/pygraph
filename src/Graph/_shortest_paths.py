# If you want to use the Graph constructor anywhere in your code.
import math, sys
# sys.path.insert(1, "../../../")
# import pygraph.src.Graph



def find_shortest_paths(self,):
    """
    Finds the shortest distance in all pairs of vertices in a weighted graph.
    Returns:
        List(List(int)): The n * n matrix delta, such that delta[i][j] = shortest distance between vertices i and j
    """
    
    

def find_shortest_paths(self,graph,s):
    """
    Returns the shortest distance from a source s to all other vertices 
        in a weighted graph.
    Uses Bellman Ford algorithm.
    Args:
        s (int): Source vertex from which shortest path lengths to all other 
                reachable vertices is to be found.
                
    Returns:
        delta (List(int)): Shortest path lengths between source s to all other 
                vertices of a weighted graph. 
    """
    #intialize distance and predecessor
    dist, pre = dict(), dict()
    for vertex in graph:
        dist[vertex], pre[vertex] = float('inf'), None
    dist[s] = 0 

    #Relax the edges
    for i in range(len(graph) - 1):
        for vertex in graph:
            for adj_vertex in graph[vertex]:
                if dist[adj_vertex] > dist[vertex] + graph[vertex][adj_vertex]:
                    dist[adj_vertex], pre[adj_vertex] = dist[vertex] + graph[vertex][adj_vertex], vertex

    #check for negative cycles
    for vertex in graph:
        for adj_vertex in graph[vertex]:
            assert dist[adj_vertex] <= dist[vertex] + graph[vertex][adj_vertex], "Negative weight cycle."
 
    return dist, pre

def find_shortest_paths(self, s, t):
    """
    Finds the shortest distance between two vertices in a weighted graph.
    Args:
        s (int): source vertex
        t (int): destination vertex
        
    Returns:
        delta (int): Shortest distance between vertex s and vertex t.
    """
    pass

