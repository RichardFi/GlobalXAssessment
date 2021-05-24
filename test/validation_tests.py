import unittest
import sys
sys.path.append("/GlobalXAssessment/name_sorter")

from validation import *

class ValidationTests(unittest.TestCase):
    def test_validate_name_valid_format(self):
        name = "Janet Parsons"
        expect = Validation().isValid(name)
        self.assertTrue(expect)

    def test_validate_name_not_only_letters(self):
        name = "Janet 1Parsons1"
        expect = Validation().isValid(name)
        self.assertFalse(expect)

    def test_validate_less_than_two_words(self):
        name = "Janet"
        expect = Validation().isValid(name)
        self.assertFalse(expect)

    def test_validate_more_than_four_words(self):
        name = "Janet Parsons Adonis Julius Archer"
        expect = Validation().isValid(name)
        self.assertFalse(expect)

if __name__ == '__main__':
    unittest.main()