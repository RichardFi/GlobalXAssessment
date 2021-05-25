class FileWrite:
    def __init__(self, fileName):
        # filename to be written
        self.fileName = fileName

    def write(self, nameList):
        with open(self.fileName, "w") as f:
            for name in nameList:
                # write a full name each line, use space to divide given names and last name
                f.write(str(name.givenNames) + ' ' + str(name.lastName) +"\n")
        return True

