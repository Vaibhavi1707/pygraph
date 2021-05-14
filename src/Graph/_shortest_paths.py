# If you want to use the Graph constructor anywhere in your code.
import math, sys
# sys.path.insert(1, "../../../")
# import pygraph.src.Graph

# Complete the functions below

def find_shortest_paths(self):
    """
    Finds the shortest distance in all pairs of vertices in a weighted graph.
    Returns:
        List(List(int)): The n * n matrix delta, such that delta[i][j] = shortest distance between vertices i and j
    """
    pass

def find_shortest_paths(self, s):
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
    pass

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

class Graph:
    def __init__(self, vertices):
        self.v = vertices #number of vertices in graph
        self.g = [] #edges list
    
    def add_edge(self,s,d,w):
        self.g.append([s,d,w])

    
    def bellman_ford(self,src):
        #for i in range(number of edges): 
        #    self.g.append([s, d, w])

        distance = float("Inf") * self.v
        distance[src] = 0
        
    def relax(self,distance) -> int:
        for i in range(self.v -1):
            for s,d,w in self.g:
                if distance[s] != float("Inf") and distance[s] + w < distance[d]:
                    distance[d] = distance[s] + w
        return distance 

    def check_neg_cycle(self,distance) -> None:
        for s, d, w in self.graph:
            if distance[s] != float("Inf") and distance[s] + w < distance[d]:
                return

    def print_output(self):
      #############
        pass        


#in progress
