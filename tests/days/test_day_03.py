import unittest
from src.days.day_03.main import solve


class TestUtility(unittest.TestCase):

    def test_solve_part1(self):
        actual = solve(1, True)
        expected = 198
        self.assertEqual(expected, actual)

    def test_solve_part2(self):
        actual = solve(2, True)
        expected = 230
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
