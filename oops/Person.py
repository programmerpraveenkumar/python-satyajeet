class Person:
    id:int
    name:str
    address:str

    def __init__(self,id,name,addres):
        self.id = id
        self.name = name
        self.address = addres
        # print("this is person constructor..")
        # print(self.id,self.address,self.name)

    def setId(self,id):
        self.id=id
    def setName(self,name):
        self.name=name
    def setAddress(self,address):
        self.address=address

    def printDetails(self):
        # return self.id,self.address,self.name
        print(self.id,self.address,self.name)
    
# object is created
p1 = Person(10,"test3","sample address")
p1.printDetails()
p1.setId(85)
p1.setName("updated..")
p1.printDetails()

p2 = Person(10,"test4","sample address2")
p2.printDetails()
    
