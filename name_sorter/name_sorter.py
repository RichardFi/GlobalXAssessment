from file_read import FileRead
from file_write import FileWrite
from name import Name
import sys

class NameSorter:
    def __init__(self, nameList):
        self.nameList = nameList

    def sort(self):
        sortedNameList = sorted(self.nameList, key=lambda x: (x.lastName.lower(), x.givenNames.lower()))
        for name in sortedNameList:
            print(name.givenNames + ' ' + name.lastName)
        return sortedNameList

def main():
   fileReader = FileRead(sys.argv[1])
   ns = NameSorter(fileReader.read())
   fileWriter = FileWrite('sorted-names-list.txt')
   fileWriter.write(ns.sort())

if __name__ == "__main__":
   main()
