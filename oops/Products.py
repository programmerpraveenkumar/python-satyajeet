class Product:
    name:str
    price:int
    def printDetails(self):
        print(self.name,self.price)

class Laptop(Product):
    _assemble_place="india"
    def calculatePrice(self,qty):
        self.printDetails()
        print(self.name," price is for ",qty,(qty*self.price))


laptop_obj = Laptop()
laptop_obj.name = "dell"
laptop_obj.price = 15000
laptop_obj.calculatePrice(5)