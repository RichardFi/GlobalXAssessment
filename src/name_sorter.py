from file_read import FileRead
from file_write import FileWrite
from print_names_list import PrintNamesList 
import sys

class NameSorter:
    def __init__(self, nameList):
        # name list to be sorted
        self.nameList = nameList

    def sort(self, reverse=False):
        # sort the name by last name first then given names
        sortedNameList = sorted(self.nameList, key=lambda x: (x.lastName.lower(), x.givenNames.lower()))
        # print sorted name list

        return sortedNameList

def main():
   fileReader = FileRead(sys.argv[1])
   #reverse = sys.argv[2]
   ns = NameSorter(fileReader.read())
   fileWriter = FileWrite('sorted-names-list.txt')
   sortedList = ns.sort()
   fileWriter.write(sortedList)
   PrintNamesList(sortedList).print_list()

if __name__ == "__main__":
   main()
