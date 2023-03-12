from unittest import TestCase
from implement import implement2


class SolutionTest(TestCase):
    def test_solution1(self):
        x, y, dir = 1, 1, 0
        field = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]
        result = implement2.solution(x, y, dir, field)
        expect = 3
        self.assertEqual(expect, result)
