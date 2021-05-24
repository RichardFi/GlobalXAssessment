import unittest
import sys
sys.path.append("/GlobalXAssessment/name_sorter")

from file_write import FileWrite
from name import Name

class FileReadTests(unittest.TestCase):
    def test_write_file(self):
        actual = ['Janet Parsons\n','Vaughn Lewis\n','Adonis Julius Archer\n','Shelby Nathan Yoder\n']

        nameList = []
        nameList.append(Name('Janet Parsons\n'))
        nameList.append(Name('Vaughn Lewis\n'))
        nameList.append(Name('Adonis Julius Archer\n'))
        nameList.append(Name('Shelby Nathan Yoder\n'))
        fileName = 'test_write.txt'
        FileWrite(fileName).write(nameList)
        with open(fileName, "r") as f:
            expect = f.readlines()
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()