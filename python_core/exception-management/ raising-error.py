try:
    age=15
    if age>10:
            # print("application is only for kids")
            raise ValueError("application is only for kids")
    else:
            print("yes you can access")
except ValueError as e:
        print("Error in ValueError",{e})

except Exception as e:
        print("Error occured",{e})        

print("application last line")


    # sender -> 10000 ..1000
    # get his current balance/only 1000rs
    # if bal>new_amount: raise valueError("balance is not enough!!!")