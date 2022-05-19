import { useEffect, useState } from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar';
import ListSubheader from '@mui/material/ListSubheader';
import SyncIcon from '@mui/icons-material/Sync';
import { faker } from '@faker-js/faker';
import { Link, useLocation } from "react-router-dom";

export function Display(){
    const [imageData, setImageData] = useState([]);
    const [images, setImages] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const location = useLocation();

    useEffect(() => {
      setTimeout(() => {
      if (images.length === 0) {
        if (!location.state.test) {loadImages(location.state.filename)}
        else {fakeImages()}
      }}
      ,10000);
    }, []);
    
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

    const fakeImages = () => {
        let pics = [];
        for (let i = 0; i < 12; i++) {
            pics.push({'image_url': faker.image.nature(820, 820, true), 'text': faker.lorem.sentence()});
        };
        setImages(displayImages(pics));
    };

    const displayImages = (pics) => {
        setIsLoading(false);
        return(
          <ImageList sx={{ width: '50vw', height: '50vh', bgcolor: '#FCF7F0'}} cols={1}>
            <ImageListItem key="Subheader" cols={1} sx={{bgcolor: '#FCF7F0'}}>
              <ListSubheader component="div" sx={{fontSize: '2vw', bgcolor: '#FCF7F0'}}>{location.state.title}</ListSubheader>
            </ImageListItem>
            {pics.map((item) => (
              <ImageListItem key={item.image_url}>
                <img
                  src={`${item.image_url}?w=164&h=164&fit=crop&auto=format`}
                  alt={''}
                  loading="lazy"
                />
                <ImageListItemBar title={item.text} sx={{fontSize: '2vw'}} position="below"></ImageListItemBar>
              </ImageListItem>
            ))}
          </ImageList>
        );
    };

    return(
        <>
            <Link to='/'>Back to menu</Link>
            {isLoading ? <><p>Loading Images...</p><SyncIcon className='loading-icon' sx={{ fontSize: 40 }}/></> : images}
        </>
    );
}