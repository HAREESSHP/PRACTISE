import { useState } from 'react'

import './App.css'

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
