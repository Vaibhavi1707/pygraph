import unittest, math, sys
sys.path.insert(1, "../../")
import pygraph.src.Graph._depth_first_traversal
from pygraph.src.Graph import Graph

class TestDepthFirstTraversal(unittest.TestCase):
    def setUp(self):
        self.graph1 = Graph([0, 1], [(0, 1), (1, 0)])
        self.graph2 = Graph([0, 1, 2, 3, 4], [(0, 1), (0, 2), (2, 1), (3, 1), (3, 2), (2, 4), (3, 4)])
        self.graph3 = Graph([0, 1, 2, 3, 4], [(0, 1), (0, 2), (2, 3), (2, 4)])
    
    def test_depth_first_search(self):
        self.assertEqual(self.graph1.depth_first_search(), )
    
    def test_topological_sort(self):
        self.assertEqual(self.graph2.topological_sort(), [0, 3, 2, 1, 4])

if __name__ == '__main__':
    unittest.main()
    