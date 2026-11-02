// array
numList=[5,10,9]
personList=["test","abc","oiuyiuoy","tree"]

newList= numList.filter(n=>{
    return n%2==0
}
)
console.log(newList);


newpersonList = personList.filter(n=>n.startsWith("a"))
console.log(newpersonList);