import unittest
from src.year_2021.day_06.main import solve


class TestUtility(unittest.TestCase):

    def test_solve_part1(self):
        actual = solve(1, True)
        expected = 5934
        self.assertEqual(expected, actual)

    def test_solve_part2(self):
        actual = solve(2, True)
        expected = 26984457539
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
