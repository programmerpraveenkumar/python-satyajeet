# try except
try:
    userlist = ["rt","rter",'yu']
    print(userlist[1])
    res = 4/0
except IndexError as e:
    print("error occured",{e})   

except ZeroDivisionError as e:
    print("error occured",{e})   

except Exception as e:
    print("error occured",{e})

print("this is the last line")