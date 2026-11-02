let firstname = "adsf asdf ";
console.log(firstname.toUpperCase())
console.log(firstname.toLowerCase())
// split the string by `s` return array
let sp = firstname.split("s")

//start from the position 2
let subs = firstname.substring(2)

console.log(sp);
console.log(subs);
// /length of the string
console.log(firstname.length);

//check starts with any string
console.log(firstname.startsWith("abc"));

//remove the whitespce from first and last
console.log(firstname.trim().length);
console.log(firstname.trimStart().length);
console.log(firstname.trimEnd().length);


let age = "56";
let address = "door132"

// isNaN(str)->isNot a Number->return boolean

console.log(isNaN(age));
console.log(isNaN(address));






