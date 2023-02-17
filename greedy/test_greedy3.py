from unittest import TestCase
from greedy import greedy3


class SolutionTest(TestCase):
    def test_solution1(self):
        result = greedy3.solution(25, 5)
        expect = 2
        self.assertEqual(expect, result)

    def test_solution2(self):
        result = greedy3.solution(17, 4)
        expect = 3
        self.assertEqual(expect, result)

    def test_solution3(self):
        result = greedy3.solution(25, 3)
        expect = 6
        self.assertEqual(expect, result)