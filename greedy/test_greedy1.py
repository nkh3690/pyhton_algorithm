from unittest import TestCase
from greedy import greedy1


class SolutionTest(TestCase):
    def test_solution1(self):
        result = greedy1.solution(8, 3, [2, 4, 5, 4, 6])
        expect = 46
        self.assertEqual(expect, result)

    def test_solution2(self):
        result = greedy1.solution(7, 2, [3, 4, 3, 4, 3])
        expect = 28
        self.assertEqual(expect, result)
