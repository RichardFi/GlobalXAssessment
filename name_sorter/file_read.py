from name import Name
from validation import Validation

class FileRead:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            text = f.readlines()

        nameList = []
        for name in text:
            if Validation().isValid(name.strip()):
                nameList.append(Name(name.strip()))
            else:
                print('Ignored as invalid name format: ' + name)
        return nameList

