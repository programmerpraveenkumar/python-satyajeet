import { useState } from 'react'
import './about.css'
import MenuComponent from './MenuComponent';
function AboutComponent(){
  const [step,setStep]=useState(1);
return(
    <>
        <MenuComponent myCurrentPage="about"/>
      <button className='btn btn-danger'>Click Me</button>
      {step}
      <h1 className=''>this is about</h1>
      <h2 className={(step % 2 ==0)?'my-class':'my-class2'}>this is another heading</h2>
      <button onClick={()=>setStep(val=>val+1)}>Increment</button>

      <div class="card" className='card-style'>
    <img src="https://picsum.photos/200/300" class="card-img-top" alt="..."/>
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>

<div class="alert alert-success" role="alert">
  A simple primary alert—check it out!
</div>
    </>
  )
}

export default AboutComponent