function add(a,b){
    console.log(a+b);
    
    console.log("inside the add");
}
console.log("start");
//declare the method in settimeout
//2nd param is timeout in ms
// arrow function =>
setTimeout(()=>{add(1,2)},1000*5)
// setTimeout(function(){add(1,2)},1000*5)
// console.log("end");

// setInterval(add,1000*5)