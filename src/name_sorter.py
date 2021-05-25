from file_read import FileRead
from file_write import FileWrite
import sys

class NameSorter:
    def __init__(self, nameList):
        # name list to be sorted
        self.nameList = nameList

    def sort(self):
        # sort the name by last name first then given names
        sortedNameList = sorted(self.nameList, key=lambda x: (x.lastName.lower(), x.givenNames.lower()))
        # print sorted name list
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
