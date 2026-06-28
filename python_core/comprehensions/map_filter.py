
# def myLogic(x,y):
nameList = ['1-test1','2test','3-test3']
map_obj=map(len,nameList)
list_obj = list(map_obj)
print(list_obj)

def myLogic(x):
    return x*x
    
 
numList=[1,2,3,5,8]

map_obj=map(myLogic,numList)
list_obj = list(map_obj)
print(list_obj)

def myLogic1(x):
    res=(x*x)+10
    if(res>50):
        return res
    

filter_list = list(filter(myLogic1,numList))
print(filter_list)