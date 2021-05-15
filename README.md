<div align="center"><h1>Pygraph</h1></div>
<div align="center">
<a href="https://www.python.org/"><img src=https://forthebadge.com/images/badges/made-with-python.svg ></a>
</div>
This package implements basic graph and shortest path algorithms.
This project has 3 functions namely:
- [_breadth_first_traversal.py ](https://github.com/Vaibhavi1707/pygraph/blob/main/src/Graph/_breadth_first_traversal.py): It performs breadth first search on the given graph.Requirements being source vertex(int) from which breadth first search to be performed.It returns frontier_from_src, parent (tuple(List(int), List(int)) i.e. the level of each reachable vertex in the BFS tree and parent of each vertex found during the traversal.
- [_depth_first_traversal.py](https://github.com/Vaibhavi1707/pygraph/blob/main/src/Graph/_depth_first_traversal.py): As the name suggests it performs depth first search on the given graph.Requirements being source vertex(int) from which depth first search to be performed.It returns predecessor (List[int]), topo_order (List[int]) i.e. List of dfs predecessors such that predecessor[i] = predecessor of i found during DFS traversal and topo sort of the graph obtained.
- [_shortest_paths.py ](https://github.com/Vaibhavi1707/pygraph/blob/main/src/Graph/_shortest_paths.py) It performs Bellman-Ford algorithm on the given graph taking source vertex as input requirement and returns dist (List(int)), pre (List(int)) i.e. Shortest path lengths between source s to all other vertices of a weighted graph and predecessor in the path from s to each vertex respectively.


### Directory Structure
```
pygraph/
|
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
├── setup.py
├── src
|   ├── Graph
|   |   ├── __init__.py
|   |   ├── _breadth_first_traversal.py
|   |   ├── _depth_first_traversal.py
|   |   └── _shortest_paths.py
└── tests
    ├── _bfs_test.py
    ├── _dfs_test.py
    └── _shortest_paths_test.py


```
## Authors

- Mahi Monga: [Github](https://github.com/mahimonga) [Linkedin](https://www.linkedin.com/in/mahimonga/)
- Vaibhavi Lokegaonkar: [Github](https://github.com/Vaibhavi1707) [Linkedin](https://www.linkedin.com/in/vaibhavi-lokegaonkar-06b844195/)
- Tanmayee Pemmaraju: [Github](https://github.com/priyansi) [Linkedin](https://www.linkedin.com/in/tanmayee-pemmaraju-2abb841aa/)


## License

All rights reserved. Licensed under the MIT License.

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
