import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        n = "101101101"
        x = 5
        self.assertEqual(Solution.solve(n, x), 3)

    def test_case_2(self):
        n = "1111101"
        x = 5
        self.assertEqual(Solution.solve(n, x), 1)

    def test_case_3(self):
        n = "110011011"
        x = 5
        self.assertEqual(Solution.solve(n, x), 3)
