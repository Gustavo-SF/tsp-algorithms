import unittest

import tsp_algorithms as tsp


cost_matrix =[
    [0.0, 10.0, 5.0, 7.0, 8.0, 8.0],
    [10.0, 0.0, 7.0, 5.0, 10.0, 8.0],
    [5.0, 7.0, 0.0, 6.0, 3.0, 2.0],
    [7.0, 5.0, 6.0, 0.0, 4.0, 2.0],
    [8.0, 10.0, 3.0, 4.0, 0.0, 2.0],
    [8.0, 8.0, 2.0, 2.0, 2.0, 0.0],
]

class TestTSPAlgorithms(unittest.TestCase):
    def test_nearest_neighbors(self):
        route = tsp.nn(cost_matrix)
        assert route == [1, 3, 5, 2, 4, 0]
    
    def test_2opt(self):
        route = [1, 3, 5, 2, 4, 0]
        route_opt = tsp.two_opt(cost_matrix, route)
        assert route_opt == [1, 3, 5, 4, 2, 0]
    

if __name__ == '__main__':
    unittest.main()
