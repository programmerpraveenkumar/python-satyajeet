import HomeComponent from "./Home"
import AboutComponent from "./About"
import { BrowserRouter, Route, Router, Routes } from "react-router-dom"
import 'bootstrap/dist/css/bootstrap.min.css';
// function App() {
//   //  /getuser from api
//   // store user data to api
//   return(
//     <>
//     <h1>this is my page</h1>
//         {/* html form code */}
//     </>
//   )
// }
//   return (

function App() {

  return (
    <>
     <BrowserRouter>
      <Routes>
          <Route path="/" element={<HomeComponent/>}/>
          <Route path="home" element={<HomeComponent/>}/>
          <Route path="about" element={<AboutComponent/>}/>
          <Route path="*" element={<h1>No Page found</h1>}/>
      </Routes>
     </BrowserRouter>
    </>
  )
}





export default App
