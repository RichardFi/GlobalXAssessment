import unittest
import sys
import os
sys.path.append(os.path.abspath("./src"))

from name import Name

class FileReadTests(unittest.TestCase):
    def test_name_given_names(self):
        name ='Adonis Julius Archer'
        actual = 'Adonis Julius'

        expect = Name(name).givenNames
        self.assertEqual(actual, expect)

    def test_name_last_name(self):
        name ='Adonis Julius Archer'
        actual = 'Archer'

        expect = Name(name).lastName
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()