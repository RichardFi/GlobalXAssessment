class FileWrite:
    def __init__(self, fileName):
        self.fileName = fileName

    def write(self, nameList):
        with open(self.fileName, "w") as f:
            for name in nameList:
                f.write(str(name.givenNames) + ' ' + str(name.lastName) +"\n")
        return True

