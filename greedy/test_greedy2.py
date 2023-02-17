from unittest import TestCase
from greedy import greedy2


class SolutionTest(TestCase):
    def test_solution1(self):
        array = [
            [3, 1, 2],
            [4, 1, 4],
            [2, 2, 2]
        ]
        result = greedy2.solution(3, 3, array)
        expect = 2
        self.assertEqual(expect, result)

    def test_solution2(self):
        array = [
            [7, 3, 1, 8],
            [3, 3, 3, 4]
        ]
        result = greedy2.solution(2, 4, array)
        expect = 3
        self.assertEqual(expect, result)
