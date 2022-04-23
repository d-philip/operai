import './App.css';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import Paper from '@mui/material/Paper';
import SyncIcon from '@mui/icons-material/Sync';
import { useEffect, useState } from 'react';

function App() {
  const [imageData, setImageData] = useState([]);
  const [images, setImages] = useState([]);

  useEffect(() => {
    loadImages()
  }, []);

  const loadImages = () => {
    const apiURL = 'http://127.0.0.1:5000/';
    fetch(apiURL + 'images')
      .then(resp => resp.json())
      .then(data => setImageData(data.images))
      .then(setImages(displayImages(imageData)))
      .catch(err => console.log(err))
  };

  const displayImages = (pics) => {
    return(
      <ImageList sx={{ width: 500, height: 450 }} cols={3} rowHeight={164}>
        {pics.map((item) => (
          <ImageListItem key={item}>
            <img
              src={`${item}?w=164&h=164&fit=crop&auto=format`}
              alt={''}
              loading="lazy"
            />
          </ImageListItem>
        ))}
      </ImageList>
    );
  };

  return (
    <div className="App">
      <Paper elevation={2} className='main-container'>
        {images === [] ? <SyncIcon className='loading-icon' sx={{ fontSize: 40 }}/> : images}
      </Paper>
    </div>
  );
}

export default App;
