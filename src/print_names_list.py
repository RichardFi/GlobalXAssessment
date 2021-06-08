class PrintNamesList:
    def __init__(self, nameList):
        # name list to be sorted
        self.nameList = nameList

    def print_list(self):
        for name in self.nameList:
            print(name.givenNames + ' ' + name.lastName)
