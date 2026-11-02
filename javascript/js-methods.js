
let monthFull = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Dec"]

// date methods
let d = new Date();
console.log(d.getDate());
console.log(monthFull[d.getMonth()]);
console.log(d.getFullYear());
console.log(d.getDay());
console.log(d.getDate()+"-"+monthFull[d.getMonth()]+"-"+d.getFullYear());
console.log(
d.getHours(),
d.getMinutes(),
d.getSeconds())