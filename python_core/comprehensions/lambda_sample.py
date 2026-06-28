
# def myLogic(x,y):

# def myLogic(x):
#     return x*x
    # res=(x*x)+10
    # if(res>50):
    #     return res
    # return 0

# sqrt = [lambda x:myLogic(x) for x in numList]
# map(logic,)
# print(sqrt)


# mul = lambda a,b:a*b
# print(mul(5,8))



# map(lambda x: x*x, numList) creates a map object.
# list(...) converts the map object into a list of results.
# res = map(lambda x:x*x,numList)
#list_res list(res)

numList=[1,2,3,5,8]
a = lambda x:x*x
print(a(5))
map_obj=map(a,numList)
list_obj = list(map_obj)
print(list_obj)

filter_list = list(filter(lambda a:a%2==0,numList))
print(filter_list)
# map,filter