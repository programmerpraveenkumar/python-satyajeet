import { useEffect, useRef, useState } from "react";
import MenuComponent from "./MenuComponent";

function HomeComponent(){
  // below variables will not update and in ui
  let msg = "hi";
  let personList = ['adf','swerfert','ioewuhrdisu']

  // reference the html element to the react
  // using ref we can have js functions in react
  const h1_ref = useRef();
  // state variable will help to update in ui 
  // useState
  const [firstName,setFirstName] = useState('how are you..');
  const [password,setPassword] = useState('');
  const [age,setAge] = useState('');
  const [mobile,setMobile] = useState('');
  const [email,setEmail] = useState('');
  const [salary,setSalary] = useState('');
  const [emp_id,setEmpId] = useState('');
  const [user_list,setUserList] = useState([]);

  const [new_form,setNewForm]= useState({
    "first_name":"",
    "emp_id":"",
    "email":"",
    "salary":""
  })


  // arrow function
  const handleChange=(e)=>{
      setNewForm({
        ...new_form,
       [e.target.name]:e.target.value
      })
  }


   const printState=(e)=>{
      console.log(new_form);
  }
  // const base_url = "http://127.0.0.1:8000/user/"
  const base_url = "http://32.236.127.237:8081/api/user";


  //  load only once during the page loading
  useEffect(()=>{
    console.log("from use effect")
  },[])

  // whenever state variable changes below will trigger
  useEffect(()=>{
    console.log("changing firstName ",firstName)
    // write the text into the html element
    h1_ref.current.innerHTML = firstName; 
  },[firstName])


  const getUserData=async()=>{
    // to call the apis
    // axios
    let response =  await fetch(base_url,
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
      "age":age,
      "mobile":Number(mobile),
      "password":password,
    };
    let response =  await fetch(base_url,
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
            <h1>this is my home Component new deployment</h1>
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
                <b className={(ele?.salary>50000)?'highlight':null}>Name</b>:{ele?.name} <br/>
                <b>Id</b>: {ele?.id}<br/>
                <b>Salary</b>: {ele?.salary}<br/>
                <b>Email</b>: {ele?.email}<br/>

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
        <input onChange={(e)=>setMobile(e.target.value)} type="text" placeholder="Enter Mobile" />
        <input onChange={(e)=>setAge(e.target.value)} type="text" placeholder="Enter age" />
        <input onChange={(e)=>setPassword(e.target.value)} type="password" placeholder="Enter Password" />
        
        {/* reference the html to react using useref */}
        <h1 ref={h1_ref}>this is simpel h1</h1>
          
        {/* always register the function from button click in react */}
        <button onClick={storeUserData}> Store Emp Details</button>
        <button onClick={getUserData}>Click to get user data</button>

        <h1>new Form</h1>
        <input name="first_name" onChange={ handleChange} type="text" placeholder="Enter First name" />
        <input name="emp_id" onChange={handleChange } type="text" placeholder="Enter Emp id" />
        <input name="email" onChange={ handleChange} type="text" placeholder="Enter email" />
        <input name="salary" onChange={ handleChange} type="text" placeholder="Enter salary" />
        <button onClick={printState}>Check common useState</button>
    </>
  )
}

export default HomeComponent;