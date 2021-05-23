from name import *
from validation import *

class FileRead:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            text = f.readlines()

        nameList = []
        for name in text:
            if Validation(name.strip()).isValid():
                nameList.append(Name(name.strip()))
            else:
                print('Ignored as invalid name format: ' + name)
        return nameList

