import re

class Validation:
    def isValid(self, name):
        # use regex to check if a name only contain letters and space
        if not bool(re.match('^[a-zA-Z ]+$',name)):
            return False
            
        # check if name is more than 1 word and less than 4 words 
        # as a name contain at least 1 last name and 1 given name and maximium 3 given names
        if len(name.split()) < 2 or len(name.split()) > 4:
            return False
        return True
