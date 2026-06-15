userlist=[
{
    "name":"test1",'age':15,"mobile":5656
}
,
{
    "name":"test2",'age':16,"mobile":5656
}
,
{
    "name":"test3",'age':17,"mobile":445656
}
,
{
    "name":"test4",'age':18,"mobile":8965656
}
]

for user in userlist:
    print("."*10)
    print(user['name'],user['age'])
    # for key,value in user.items():
    #     print(key,value)