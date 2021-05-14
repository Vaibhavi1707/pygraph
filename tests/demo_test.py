#for bellman-ford
def test():
    graph = {
        'a': {'c': 3},
        'b': {'a': 2},
        'c': {'b': 7, 'd': 1},
        'd': {'a': 6},
    } 
    assert dist == {
        'a': 0,
        'b': 10,
        'c': 3,
        'd': 4
        }
    assert pre == {
        'a': None,
        'b': 'c',
        'c': 'a',
        'd': 'c'
        }
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
        }

    dist, pre = bellman_ford(graph, 'a')

    assert dist == {
        'a':  0,
        'b': -1,
        'c':  2,
        'd': -2,
        'e':  1
        }

    assert pre == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
        }
test()
