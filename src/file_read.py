from name import Name
from validation import Validation

class FileRead:
    def __init__(self, filename):
        # filename to be read
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            text = f.readlines()

        nameList = []
        for name in text:
            # check if a name is valid, if not ignore it
            if Validation().isValid(name.strip()):
                nameList.append(Name(name.strip()))
            else:
                print('Ignored as invalid name format: ' + name)
        return nameList

