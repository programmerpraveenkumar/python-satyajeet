 
class Laptop :
    __assemble_place="india"
    def printPlace(self,place):
       self.__assemble_place = place
       self.__print()

    def __print(self):
        print("from print method ",self.__assemble_place)
    

lap_obj = Laptop()
# lap_obj.__assemble_place= "update"
lap_obj.printPlace("update")
lap_obj.__print()