from unittest import TestCase
from implement import implement1


class SolutionTest(TestCase):
    def test_solution1(self):
        result = implement1.solution('a1')
        expect = 2
        self.assertEqual(expect, result)

    def test_solution2(self):
        result = implement1.solution('c2')
        expect = 6
        self.assertEqual(expect, result)

    def test_solution3(self):
        result = implement1.solution('h8')
        expect = 2
        self.assertEqual(expect, result)