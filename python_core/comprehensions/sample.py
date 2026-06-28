list = ['test1','2test','test3']
list2 = [1,2,3,4,4,5,6]
# comprehension is writing the logic in one line
new_filter ={item for item in list if item.startswith('t')}
print(new_filter)
new_filter = {item for item in list2 if item %2 ==0 and item > 2}
print(new_filter)
squar={x:x**2 for x in range(2,5)}
print(squar)

nameList = ['1-test1','2-2test','3-test3']
nameSplit = {n[0]:n.split("-")[1] for n in nameList}

nameSplit2 = [n.split("-")[1] for n in nameList]

print(nameSplit2)

nameList2 = ['est1','st','t23']
nameSplit3 = {len(n):n for n in nameList2}
print(nameSplit3)