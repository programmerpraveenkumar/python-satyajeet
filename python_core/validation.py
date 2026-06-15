age:str="55j"

if age.isdigit():
    # string to int data type
    age_int = int(age)
    print(type(age_int))

print(age.isdigit())
print(age.isalpha())
print(age.isdecimal())

num:int = 45
numstr = "48"
# int to float
numf:float = float(num)
numstrf:float = float(numstr)
print(numstrf)