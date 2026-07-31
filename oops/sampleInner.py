# outer class
class City:
    name=None
    def prinName(self):
        print(self.name)

    # innr class
    class Mumbai:
        peopleCount=4000
        def printCount(self,outer_obj):
            outer_obj.name="mumbai"
            print(outer_obj.name,self.peopleCount)
    class Banglore:
        peopleCount=4000
        def printCount(self,outer_obj):
            outer_obj.name="banglore"
            print(outer_obj.name,self.peopleCount)
        # define methods

city_obj = City()
# using  city_obj creating mumbai
mumbai_obj = city_obj.Mumbai()
mumbai_obj.printCount(city_obj)

b_obj = city_obj.Banglore()
b_obj.printCount(city_obj)