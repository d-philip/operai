import './App.css';
import Paper from '@mui/material/Paper';
import { useEffect, useState } from 'react';
import { Display } from './Display';


function App() {

  useEffect(() => {

  }, []);

  return (
    <div className="App">
      <Paper elevation={2} className='main-container'>
        <h1>OperAI</h1>
        <Display/>
      </Paper>
    </div>
  );
}

export default App;
