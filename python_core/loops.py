# print(range(0,5))
x:float = 2.5
for x in range(2,10):
    print(x)

print(x)


userlist=["test1",1,1.5,"safsf"]
usersdetails = {
    "name":"test",'age':15,"mobile":565656
}
for user in userlist:
    print(user)

print(type(usersdetails))


for key,value in usersdetails.items():
    print(key,"--",value)