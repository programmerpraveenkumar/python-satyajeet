import { useState } from "react";
import MenuComponent from "./MenuComponent";

function HomeComponent(){
  // below variables will not update and in ui
  let msg = "hi";
  let personList = ['adf','swerfert','ioewuhrdisu']
  // state variable will help to update in ui 
  // useState
  const [firstName,setFirstName] = useState('how are you..');
  const [password,setPassword] = useState('');
  const [email,setEmail] = useState('');
  const [salary,setSalary] = useState('');
  const [emp_id,setEmpId] = useState('');
  const [user_list,setUserList] = useState([]);



  const getUserData=async()=>{
    // to call the apis
    // axios
    let response =  await fetch("http://127.0.0.1:8000/user/",
      {
        method:"GET",
        "headers":{"token":"random-value"}
      });
    let json_data = await response.json();
    // if server is success response
    if (response.ok){
      console.log(json_data);
      setUserList(json_data);
    }else{
      alert("server error");
    }
    
  }


  const storeUserData=async()=>{
    let data = {
      "name":firstName,
      "emp_id":emp_id,
      "salary":salary,
      "email":email,
      "password":password,
    };
    let response =  await fetch("http://127.0.0.1:8000/user/",
      {
        "method":"POST",
        "body":JSON.stringify(data),
        "headers":{"token":"random-value","content-type":"application/json"}
      });
    // let json_data = await response.json();
    if(response.ok){
      getUserData()
    }else{
      alert("error in storing");
    }
    // console.log(json_data);
  }

  // arrow function
  const changeFirstName=()=>{
    setFirstName("new name");
  }

  return (
    <>
        <MenuComponent myCurrentPage="home"/>
            <h1>this is my home Component</h1>
        <h2>Message is {msg}</h2>
        <ul>
        {
          personList.map((ele)=>{
            return <li>{ele}</li>
          })
        }
        </ul>
        <ul>
          {
            user_list.map((ele)=>{
              return <li >
                <b className={(ele.salary>50000)?'highlight':null}>Name</b>:{ele.name} <br/>
                <b>Id</b>: {ele.emp_id}<br/>
                <b>Salary</b>: {ele.salary}<br/>
                <b>Email</b>: {ele.email}<br/>

                </li>
            })
          }
        </ul>
        <h1>  {firstName}</h1>
        {firstName}
        {/* onchange will work whenver value changes in the input */}
        <input onChange={(e)=>setFirstName(e.target.value)} type="text" placeholder="Enter First name" />
        <input onChange={(e)=>setEmpId(e.target.value)} type="text" placeholder="Enter Emp id" />
        <input onChange={(e)=>setEmail(e.target.value)} type="text" placeholder="Enter email" />
        <input onChange={(e)=>setSalary(e.target.value)} type="text" placeholder="Enter salary" />
        <input onChange={(e)=>setPassword(e.target.value)} type="password" placeholder="Enter Password" />

        {/* always register the function from button click in react */}
        <button onClick={storeUserData}> Store Emp Details</button>
        <button onClick={getUserData}>Click to get user data</button>
    </>
  )
}

export default HomeComponent;