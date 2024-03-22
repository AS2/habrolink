import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';

function App() {
 const [items, setItems] = useState([]);

   useEffect(() => {
      fetch('http://localhost:8000/items/1')
         .then((res) => res.json())
         .then((data) => {
            console.log(data);
            setItems(data);
         })
         .catch((err) => {
            console.log(err.message);
         });
   }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          I pulled from FastAPI: {JSON.stringify(items)}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
