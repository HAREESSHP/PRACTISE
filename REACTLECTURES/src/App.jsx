import { useState } from 'react'

import './App.css'
import Card from "./assets/card.jsx";

function App() {
  let [count, setCount] = useState(10)
  function increment() {
    setCount(count + 1)
  }
  function decrement() {
    setCount(count - 1)
  }

  return (
    <>
    <nav className='nav'>
      <img id="logo" src="/public/profile.jpg.png" alt="logo" className='logo' />
      <div className="nav-links">
        <button id="home" >HOME</button>
        <button id="about">ABOUT</button>
        <button id="services">SERVICES</button>
        <button id="contact">CONTACT</button>
      </div>
    </nav>
    <h1>NORMAL PRACTICE</h1>
    <p>These is an incrementer</p>
    <p>value : <span  style={{ color: 'orange' }}>{count}</span></p>
    <br />
    <div className="buttons">
     <button className="button" onClick={increment}>INCREMENT</button>
     <button className='button' onClick={decrement}>DECREMENT</button>
    </div>
    </>
  )
}

export default App
