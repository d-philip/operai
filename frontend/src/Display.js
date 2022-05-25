import { useEffect, useState } from 'react';
import { findDOMNode } from 'react-dom';
import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar';
import ListSubheader from '@mui/material/ListSubheader';
import SyncIcon from '@mui/icons-material/Sync';
import { faker } from '@faker-js/faker';
import { Link, useLocation } from "react-router-dom";

export function Display(){
    const [images, setImages] = useState([]);
    const [text, setText] = useState('');
    const [isLoading, setIsLoading] = useState(true);
    const location = useLocation();

    useEffect(() => {
      // setTimeout(() => {
      if (images.length === 0) {
        if (!location.state.test) {
          // loadImages(location.state.filename);
          fakeImages();
          loadText(location.state.filename);
        }
        else {fakeImages()}
      }}
      // ,10000);
    // }, []);
    , []);
    
    const loadImages = (file) => {
      const apiURL = 'http://127.0.0.1:5000/';
      fetch(apiURL + `images?filename=${file}`)
      // fetch(apiURL + `images/test`)
        .then(resp => resp.json())
        .then(data => displayImages(data.images))
        .then(imageDisplay => setImages(imageDisplay))
        .catch(err => {
          console.log(err);
            setIsLoading(false);
        })
    };
    
    const loadText = (file) => {
      const apiURL = 'http://127.0.0.1:5000/';
      fetch(apiURL + `text?filename=${file}`)
        .then(resp => resp.json())
        .then(data => displayText(data.synopsis_text))
        .then(textDisplay => setText(textDisplay))
        .catch(err => {
          console.log(err);
            // setIsLoading(false);
        })
    };

    const fakeImages = () => {
        let pics = [];
        for (let i = 0; i < 64; i++) {
            pics.push({'image_url': faker.image.nature(820, 820, true), 'text': faker.lorem.sentence()});
        };
        setImages(displayImages(pics));
    };

    const handleScroll = (e, target) => {
      const totalHeight = e.target.scrollHeight - e.target.clientHeight;
      console.log(totalHeight);
      const heightRatio = e.target.scrollTop / totalHeight;
      const node = document.getElementById(target);
      const elem = findDOMNode(node);
      elem.scrollTop = heightRatio * (elem.scrollHeight - elem.clientHeight);
    };

    const displayImages = (pics) => {
        setIsLoading(false);
        return(
          <ImageList
            id='image-list'
            sx={{ width: '31vw', height: '50vh', bgcolor: '#FCF7F0', overflowX: 'visible'}} 
            variant='quilted' 
            gap={6} 
            cols={3} 
            // onScroll={(e) => handleScroll(e, 'text-box')}
          >
            {pics.map((item) => (
              <ImageListItem key={item.image_url} cols={item.cols || 1} rows={item.rows || 1} sx={{ maxWidth:'10vw', height:'auto' }}>
                <img
                  src={item.image_url}
                  alt={''}
                  loading="lazy"
                />
              </ImageListItem>
            ))}
          </ImageList>
        );
    };

    const displayText = (text) => {
      let lines = text.split('\n');
      return(
        <Box 
          id='text-box'
          sx={{ width: '30vw', height: '50vh', bgcolor: '#FCF7F0', overflow: 'scroll'}}  
          onScroll={(e) => handleScroll(e, 'image-list')}
        >
          {lines.map((line) => (
            <p key={line}>{line}</p>
          ))}
        </Box>
      );
    };

    return(
        <>
            <Link to='/'>Back to menu</Link>
            <div style={{display:'flex', flexDirection:'column', justifyContent:'center'}}>
              {isLoading ? <><p>Loading Images...</p><SyncIcon className='loading-icon' sx={{ fontSize: 40 }}/></> : images}
              {text}
            </div>
        </>
    );
}