import unittest
import sys
import os
sys.path.append(os.path.abspath("./src"))

from file_read import FileRead
from name import Name

class FileReadTests(unittest.TestCase):
    def test_read_file(self):
        actual = []
        actual.append(Name('Janet Parsons'))
        actual.append(Name('Vaughn Lewis'))
        actual.append(Name('Adonis Julius Archer'))
        actual.append(Name('Shelby Nathan Yoder'))
        actual.append(Name('Marin Alvarez'))
        actual.append(Name('London Lindsey'))
        actual.append(Name('Beau Tristan Bentley'))
        actual.append(Name('Leo Gardner'))
        actual.append(Name('Hunter Uriah Mathew Clarke'))
        actual.append(Name('Mikayla Lopez'))
        actual.append(Name('Frankie Conner Ritter'))
        actual = [(x.givenNames,x.lastName) for x in actual]

        expect = FileRead('unsorted-names-list.txt').read()
        expect = [(x.givenNames,x.lastName) for x in expect]

        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()