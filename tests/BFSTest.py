import unittest, math, sys
sys.path.insert(1, "../src/Graph")
import pygraph.src.Graph._breadth_first_traversal
import pygraph.src.Graph as Graph

class TestBreadthFirstTraversal(unittest.TestCase):
    def setUp(self):
        self.graph1 = Graph([0, 1], [(0, 1), (1, 0)])
        self.graph2 = Graph([0, 1, 2, 3, 4], [(0, 1), (0, 2), (2, 1), (3, 1), (3, 2), (2, 4), (4, 3)])
        self.graph3 = Graph([0, 1, 2, 3, 4], [(0, 1), (0, 2), (2, 3), (2, 4)])
        
    def test_bfs(self):
        shortest_path_len1, parent1 = self.graph1.breadth_first_search(0)
        self.assertEquals([shortest_path_len1, parent1], [[0, 1], [None, 0]])

        shortest_path_len2, parent2 = self.graph2.breadth_first_search(4)
        self.assertEquals([shortest_path_len2, parent2], [[math.inf, 2, 2, 1, 0], [None, 3, 3, 4, None]])
        
    def test_unweighted_shortest_paths(self):
        self.assertEquals(self.graph1.unweighted_shortest_paths(0), [0, 1])
        self.assertEquals(self.graph3.unweighted_shortest_paths(0), [0, 1, 1, 2, 2])
        
    def test_bfs_tree(self):
        pre_graph1 = self.graph1.bfs_tree(0)
        self.assertEquals([pre_graph1.v, pre_graph1.edges], [[0, 1], [(0, 1)]])
        
        pre_graph2 = self.graph2.bfs_tree(4)
        self.assertEquals([pre_graph2.v, pre_graph2.edges], [[1, 2, 3, 4], [(3, 1), (3, 2), (4, 3)]])
        
    def test_is_bipartite(self):
        self.assertFalse(self.graph3.is_bipartite(0))
        self.assertTrue(self.graph3.is_bipartite(0))