// var let const

const mycountry = "india";
// mycountry ="usa"; //error one more assign or redeclaration cannt be done for const
let phone = 8787878;
phone = 7687587;//update the value

//redeclaration will not possbile
// let phone = 6453563654;//error

var firstname = "hello";
//redeclaration can be done
var firstname = "hello hi how are you";
//update the value can be done
firstname = "im fine"

// block {} and global scope
// let,const is block scope
// var is global scope

let state = "banglore"
function changeState(){
    // block scope
    let state = "mumbai";
    console.log(state);
}
changeState()
console.log(state);
