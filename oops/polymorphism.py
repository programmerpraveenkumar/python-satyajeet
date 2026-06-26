def printDetails(obj):
    obj.printname()


class dog:
    name=None
    def __init__(self,name):
        self.name=name

    def printname(self):
        print(self.name)


class cat:
    name=None
    def __init__(self,name):
        self.name=name
    def printname(self):
        print(self.name)


printDetails(dog("dog"))
printDetails(cat("cat and mouse"))

name="asdfasd"
list=[4,8,5,85]
print(len(name))
print(len(list))
