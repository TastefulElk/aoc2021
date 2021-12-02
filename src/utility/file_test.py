import unittest
from ..utility.file import read_lines, read_lines_as_numbers # not sure why the .. is needed here 🤔

class TestUtility(unittest.TestCase):

    def test_read_lines(self):
        res = read_lines("src/utility/utility_test_input.txt")
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], "abc")

    def test_read_lines_throwsIfNonExistingFile(self):
        with self.assertRaises(FileNotFoundError):
            read_lines("src/utility/utility_test_input_non_existing.txt")

        with self.assertRaises(FileNotFoundError):
            read_lines("")

    def test_read_lines_as_numbers(self):
        res = read_lines_as_numbers("src/utility/utility_test_input_numbers.txt")
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], 123)
        self.assertEqual(res[2], -789)

if __name__ == '__main__':
    unittest.main()