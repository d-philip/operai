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
    const [isLoading, setIsLoading] = useState(false);
    const location = useLocation();

    useEffect(() => {
        // loadImages();
        if (location.state.test) {loadImages()}
        else {fakeImages()}
      }, []);
    
    const loadImages = () => {
      setIsLoading(true);
      const apiURL = 'http://127.0.0.1:5000/';
      fetch(apiURL + 'images/test')
        .then(resp => resp.json())
        .then(data => displayImages(data.images))
        .then(imageDisplay => setImages(imageDisplay), setIsLoading(false))
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
        return(
          <ImageList sx={{ width: 500, height: 450 }} cols={1}>
            <ImageListItem key="Subheader" cols={1}>
              <ListSubheader component="div">{location.state.title}</ListSubheader>
            </ImageListItem>
            {pics.map((item) => (
              <ImageListItem key={item.image_url}>
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
            <Link to='/'>Back to menu</Link>
            {isLoading ? <><p>Loading Images...</p><SyncIcon className='loading-icon' sx={{ fontSize: 40 }}/></> : images}
        </>
    );
}