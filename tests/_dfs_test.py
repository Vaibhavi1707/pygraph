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
        pre1, topo1 = self.graph1.depth_first_search()
        self.assertEqual(pre1, [None, 0])
        
        pre2, topo2 = self.graph3.depth_first_search()
        self.assertEqual(pre2, [None, 0, 0, 2, 2])
            
    def test_topological_sort(self):
        self.assertIsNone(self.graph1.topological_sort())
        topo = self.graph2.topological_sort()
        is_topo_corr = True
        for u, v in self.graph2.e:
            if topo.index(u) > topo.index(v):
                is_topo_corr = False
        self.assertTrue(is_topo_corr)
        
    def test_is_cyclic(self):
        self.assertTrue(self.graph1.is_cyclic())
        self.assertFalse(self.graph2.is_cyclic())

if __name__ == '__main__':
    unittest.main()
    