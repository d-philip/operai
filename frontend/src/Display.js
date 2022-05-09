import { useEffect, useState } from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar';
import ListSubheader from '@mui/material/ListSubheader';
import SyncIcon from '@mui/icons-material/Sync';
import { faker } from '@faker-js/faker';

export function Display(){
    const [imageData, setImageData] = useState([]);
    const [images, setImages] = useState([]);

    useEffect(() => {
        // loadImages();
        // fakeImages();
      }, []);
    
    const loadImages = () => {
    const apiURL = 'http://127.0.0.1:5000/';
    fetch(apiURL + 'images')
        .then(resp => resp.json())
        .then(data => setImageData(data.images))
        .then(setImages(displayImages(imageData)))
        .catch(err => console.log(err))
    };

    const fakeImages = () => {
        let pics = [];
        for (let i = 0; i < 12; i++) {
            pics.push({'image_url': faker.image.nature(820, 820, true), 'text': faker.lorem.sentence()});
        };
        setImages(displayImages(pics));
    };

    const displayImages = (pics) => {
        return(
          <ImageList sx={{ width: 500, height: 450 }} cols={3} rowHeight={164}>
            <ImageListItem key="Subheader" cols={3}>
              <ListSubheader component="div">Opera Name</ListSubheader>
            </ImageListItem>
            {pics.map((item) => (
              <ImageListItem key={item.text}>
                <img
                  src={`${item.image_url}?w=164&h=164&fit=crop&auto=format`}
                  alt={''}
                  loading="lazy"
                />
                <ImageListItemBar subtitle={item.text}></ImageListItemBar>
              </ImageListItem>
            ))}
          </ImageList>
        );
    };

    return(
        <>
            {images === [] ? <SyncIcon className='loading-icon' sx={{ fontSize: 40 }}/> : images}
        </>
    );
}