class Detail{
    address;
    phone;
}
class Person extends Detail{

    // will be called during the object creation
    constructor(){
        // calling parent class constructor
        super();
        console.log("this is constructor");
    }
    printMsg(msg){
        console.log(msg);
        console.log(this.address,this.phone);
    }
}

let person_obj = new Person();
// calling parent class variables
person_obj.address = "#2334,myaddress";
person_obj.phone = 9887878
person_obj.printMsg("hi good morning")
