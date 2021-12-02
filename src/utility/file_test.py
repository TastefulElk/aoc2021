import unittest
from ..utility.file import read_lines # not sure why the .. is needed here 🤔

class TestUtility(unittest.TestCase):

    def test_read_lines_from_file(self):
        res = read_lines("src/utility/utility_test_input.txt")
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], "abc")

    def test_read_lines_from_file_throwsIfNonExistingFile(self):
        with self.assertRaises(FileNotFoundError):
            read_lines("src/utility/utility_test_input_non_existing.txt")

        with self.assertRaises(FileNotFoundError):
            read_lines("")

if __name__ == '__main__':
    unittest.main()