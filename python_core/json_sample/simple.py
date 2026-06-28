import json
# 
"""
json
    1.key and value
    2.array
"""
person = '{"name":"hello","addrss":"sample","mobile":"565656"}'
# numList
print(type(person))
py_obj = json.loads(person)
print(type(py_obj))