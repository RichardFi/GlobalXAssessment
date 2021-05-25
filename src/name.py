class Name:
    def __init__(self, fullName):
        # the last word in a name is last name and others are given names
        self.givenNames = " ".join(i for i in fullName.split()[:-1])
        self.lastName = fullName.split()[-1]
