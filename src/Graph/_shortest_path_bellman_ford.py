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
