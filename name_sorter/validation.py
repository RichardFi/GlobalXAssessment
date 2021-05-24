import re

class Validation:
    def isValid(self, name):
        if not bool(re.match('^[a-zA-Z ]+$',name)):
            return False
        if len(name.split()) < 2 or len(name.split()) > 4:
            return False
        return True
