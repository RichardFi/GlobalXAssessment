import unittest
import sys
import os
sys.path.append(os.path.abspath("./src"))

from name_sorter import NameSorter
from name import Name

class NameSorterTests(unittest.TestCase):
    def test_name_sorter_by_last_name(self):
        actual = []
        actual.append(Name('Marin Alvarez'))
        actual.append(Name('Adonis Julius Archer'))
        actual.append(Name('Vaughn Lewis'))
        actual.append(Name('Janet Parsons'))
        actual = [(x.givenNames,x.lastName) for x in actual]

        expect = NameSorter([Name('Marin Alvarez'),Name('Adonis Julius Archer'),Name('Vaughn Lewis'),Name('Janet Parsons')]).sort()
        expect = [(x.givenNames,x.lastName) for x in expect]

        self.assertEqual(actual, expect)

    def test_name_sorter_by_last_name_then_given_names(self):
        actual = []
        actual.append(Name('Marin Alvarez'))
        actual.append(Name('Vaughn Alvarez'))
        actual.append(Name('Adonis Julius Archer'))
        actual.append(Name('Janet Parsons'))
        actual = [(x.givenNames,x.lastName) for x in actual]

        expect = NameSorter([Name('Marin Alvarez'),Name('Janet Parsons'),Name('Vaughn Alvarez'), Name('Adonis Julius Archer')]).sort()
        expect = [(x.givenNames,x.lastName) for x in expect]

        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()