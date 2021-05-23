class Name:
    def __init__(self, fullName):
        self.givenNames = " ".join(i for i in fullName.split()[:-1])
        self.lastName = fullName.split()[-1]
