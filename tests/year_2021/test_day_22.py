import unittest
from src.year_2021.day_22.main import solve


class TestUtility(unittest.TestCase):

    def test_solve_part1(self):
        actual = solve(1, True)
        expected = 474140
        self.assertEqual(expected, actual)

    def test_solve_part2(self):
        actual = solve(2, True)
        expected = 2758514936282235
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
