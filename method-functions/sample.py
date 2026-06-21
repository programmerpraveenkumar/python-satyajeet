# what is function?
"""
resuable logic
define the function
function will execute only calling
functions with param and without param
inside the function we can return or it may be void also
"""

def print_name():
    print("this is my function")

print("this is my function1")
    

def print_details(name,mobile):
    print(name,mobile)
    
print_details("test",45748858)
# print_name()

def add(a,b):
    print(a+b)
    return a+b#execution stopcs here
    # print(a+b)  executon will not happen at all

def add(a,b,c):
    print(a+b+c)

res = add(5,4)
print(res)
print(add(5,4))
print(add(5,4,8))
