function add(a,b){
    console.log(a,b);
    return a+b
}
// add(1,2);
// console.log(add(1,2));

async function getData(){
    console.log("calling rest api");
    let response = await fetch("https://www.apirequest.in/api/user",{"method":"GET"});
    if(response.ok){
        // response.status
         let jsonData = await response.json();
        console.log(jsonData);
    }else{
        console.log("error");
    }
}
getData();
add(1,2);



console.log("asdfasdf");
