import { useEffect, useState } from 'react';
import { faker } from '@faker-js/faker';
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import { useNavigate } from "react-router-dom";

export function Menu() {
    const navigate = useNavigate();

    return (
        <Box sx={{ width: '100%', maxWidth: '30vw', bgcolor: 'background.paper' }}>
            <List>
                <ListItemButton onClick={(e) => navigate('/display', {state: {title: "H.M.S. Pinafore"}})}>
                    <ListItem disablePadding>
                        <ListItemText primary="H.M.S. Pinafore"/>
                    </ListItem>
                </ListItemButton>
                <ListItemButton onClick={(e) => navigate('/display', {state: {title: "The Departure"}})}>
                    <ListItem disablePadding>
                        <ListItemText primary="The Departure"/>
                    </ListItem>
                </ListItemButton>
                <ListItemButton onClick={(e) => navigate('/display', {state: {title: "Dido and Aeneas"}})}>
                    <ListItem disablePadding>
                        <ListItemText primary="Dido and Aeneas"/>
                    </ListItem>
                </ListItemButton>
            </List>
        </Box>
    );
};

