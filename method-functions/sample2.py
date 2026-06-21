"""
def sum1(*args)
**args is dict 
*args is tuple

"""

# print_name()

def add(*args):
   print(len(args))
   print(type(args))
   return args
 
add(5,4)
res = add(5,4,8,"message")
print(res)


# keyword args,params has to pass with name
def printDetails(**args):
   if "name" not in args:
      raise ValueError("name is not exist")
   print(args)

printDetails(num=1,name="sdfdsf")