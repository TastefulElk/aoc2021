import unittest
from src.year_2021.day_13.main import solve


class TestUtility(unittest.TestCase):

    def test_solve_part1(self):
        actual = solve(1, True)
        expected = 17
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
