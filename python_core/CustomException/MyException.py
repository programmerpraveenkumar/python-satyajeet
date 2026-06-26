"""
    exception always inheritded from Base Class `Exception`

"""

class ChildException(Exception):
    def __init__(self, *args):
        print("args ",args[0],args[1])
        # send the error to common email,write to the log file
        super().__init__(*args)
    pass

age  = 15

if(age>10):
    raise ChildException("this is not child","age is "+str(age))
else:
    print("this is child")