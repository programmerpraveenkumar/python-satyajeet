# variables
# methods
class User:
    name="test"
    # address="asfasdfsadfds"

    def printDetails(self,name):
        print(self.name,name)
        return self.name

# object creation
user_obj = User()
user_obj.name =  "test2"
#calling method
res = user_obj.printDetails("param")
print(res)

user_obj1 = User()
#calling method
user_obj1.printDetails("obj2")