// array
nameList=["sample",10,true]
// objects
person={
    "name":"adsfasd",
    "age":"adsfads",
    "mobile":5454545
}

// json
// array of objs
personList =[
    {
    "name":"iuygiku",
    "age":"85",
    "mobile":5454545
    },
    {
        "name":"adsfasd",
      
        "mobile":555454545
    }
]

for (index in personList){
    // console.log(index,personList[index]);
    let obj = personList[index]
    console.log(obj['name'],obj['age'].toLowerCase(),obj['mobile']);
}

console.log(nameList)