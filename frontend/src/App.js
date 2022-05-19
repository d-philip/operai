import './App.css';
import Paper from '@mui/material/Paper';
import { useEffect, useState } from 'react';
import { Display } from './Display';
import { Menu } from './Menu';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {

  useEffect(() => {

  }, []);

  return (
    <Router>
      <div className="App">
        <Paper elevation={2} className='main-container' sx={{bgcolor: '#FCF7F0'}}>
          <h1 className='page-title'>OperAI</h1>
          <Routes>
            <Route path='/display' element={<Display />}/>
            <Route path='/' element={<Menu />}/>
          </Routes>

        </Paper>
      </div>
    </Router>
  );
}

export default App;
