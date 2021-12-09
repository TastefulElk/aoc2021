import unittest
from src.days.day_08.main import solve


class TestUtility(unittest.TestCase):

    def test_solve_part1(self):
        actual = solve(1, True)
        expected = 26
        self.assertEqual(expected, actual)

    def test_solve_part2(self):
        actual = solve(2, True)
        expected = 61229
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
