import json

# list
name_list = ["sdfg","asdf"]
details = {"name":"test","address":"sample address","mobile":"878787"}

print(json.dumps(name_list))
print(type(json.dumps(name_list)))


print(json.dumps(details))
print(type(json.dumps(details)))

print(json.dumps({"num":85}))