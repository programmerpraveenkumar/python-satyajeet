// array
numList=["adsdf",5,10,9]
new_list = numList.map(n=>n*3)
console.log(new_list);

new_list2 = numList.filter(n=>{
    if (!isNaN(n)){
        return n%2!=0
    }
    return false
  
}).map(n=>n*3);

console.log(new_list2);

