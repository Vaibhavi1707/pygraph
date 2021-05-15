import unittest, math, sys
sys.path.insert(1, "../../")
import pygraph.src.Graph._shortest_paths
from pygraph.src.Graph import Graph

class TestShortestPaths(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph([0, 1], [(0, 1), (1, 0)], [[0, -2], [3, 0]])
        self.g2 = Graph([0, 1, 2, 3], [(0, 1), (0, 3), (1, 2), (2, 3)], 
                        [[0, 1, 0, -1], [0, 0, -1, 0], [0, 0, 0, -2], [0, 0, 0, 0]])
        self.g3 = Graph([0], [], [23])
        
    def test_single_source_shortest_path(self):
        self.assertEqual(self.g1.find_shortest_paths(0), ([0, -2], [None, 0]))
        self.assertEqual(self.g2.find_shortest_paths(0), ([0, 1, 0, -2], [None, 0, 1, 2]))
        self.assertEqual(self.g3.find_shortest_paths(0), ([0], [None]))
            
if __name__ == '__main__':
    unittest.main()