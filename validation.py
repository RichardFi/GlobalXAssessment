import re

class Validation:
    def __init__(self, name):
        self.name = name
    
    def isValid(self):
        if not bool(re.match('^[a-zA-Z ]+$',self.name)):
            return False
        if len(self.name.split()) < 2 or len(self.name.split()) > 4:
            return False
        return True
