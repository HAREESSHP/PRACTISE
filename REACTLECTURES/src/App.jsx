import { useState } from 'react'

import './App.css'
import Card from "./Card";

function App() {
  let [count, setCount] = useState(10)
  function increment() {
    setCount(count + 1)
  }
  function decrement() {
    setCount(count - 1)
  }
function reset() {
  setCount(0)
}
function App() {
  const students = [
    {
      name: "Hari",
      age: 21,
      department: "CSE",
      college: "GNI",
    },
    {
      name: "Rahul",
      age: 22,
      department: "ECE",
      college: "GNI",
    },
    {
      name: "Priya",
      age: 20,
      department: "AIML",
      college: "GNI",
    },
    {
      name: "Sneha",
      age: 21,
      department: "IT",
      college: "GNI",
    },
    {
      name: "Arjun",
      age: 22,
      department: "MECH",
      college: "GNI",
    },
  ];

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
     <button className='button' onClick={reset}>RESET</button>
    </div>
     <div>
      <h1>Student Cards</h1>

      {students.map((student, index) => (
        <Card
          key={index}
          name={student.name}
          age={student.age}
          department={student.department}
          college={student.college}
        />
      ))}
    </div>
  );
    </>
  )
}

export default App
