import React from 'react';
import { Link } from 'react-router-dom';

import {
    Avatar,
    Button, 
    Paper,
    Grid,
    Box,
    Typography,
    TextField,

} from '@mui/material';

const Home = () => (
    <Grid>
        <Box
            sx={{
                my: 15,
                mx: 4,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                }}>
            <Typography component="h1" variant="h3">
                Welcome to Dextera            
            </Typography>
            <Typography component="h3" variant="h5">
                The Law Firm             
            </Typography>
            
            
            <Button component={Link} 
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }} to='/login' role='button'>Login</Button>
        </Box>
    </Grid>
);

export default Home;
