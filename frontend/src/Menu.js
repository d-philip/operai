import { useEffect, useState } from 'react';
import { faker } from '@faker-js/faker';
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';
import { useNavigate } from "react-router-dom";

export function Menu() {
    const navigate = useNavigate();

    return (
        <Box sx={{ width: '100%', maxWidth: '40vw', bgcolor: '#FCF7F0' }}>
            <p>View alluring images to accompany your favorite operas! Choose a title below to get started:</p>
            <Divider sx={{marginBottom: '5vh'}}/>
            <List sx={{bgcolor: '#FCF6ED', padding: 0}}>
                <ListItemButton onClick={(e) => navigate('/display', {state: {title: "H.M.S. Pinafore", test: false, filename: 'data/hmspinafore_libretto.txt'}})}>
                    <ListItem disablePadding>
                        <ListItemText primary="H.M.S. Pinafore"/>
                    </ListItem>
                </ListItemButton>
                <Divider/>
                <ListItemButton onClick={(e) => navigate('/display', {state: {title: "The Departure from Chamounix", test: false, filename: 'data/chamounix_synopsis.txt'}})}>
                    <ListItem disablePadding>
                        <ListItemText primary="The Departure from Chamounix"/>
                    </ListItem>
                </ListItemButton>
                <Divider/>
                <ListItemButton onClick={(e) => navigate('/display', {state: {title: "Venus and Adonis", test: false, filename: 'data/venusandadonis_synopsis.txt'}})}>
                    <ListItem disablePadding>
                        <ListItemText primary="Venus and Adonis"/>
                    </ListItem>
                </ListItemButton>
                <Divider/>
                <ListItemButton onClick={(e) => navigate('/display', {state: {title: "Test Images", test: true}})}>
                    <ListItem disablePadding>
                        <ListItemText primary="Test Images"/>
                    </ListItem>
                </ListItemButton>
            </List>
        </Box>
    );
};
