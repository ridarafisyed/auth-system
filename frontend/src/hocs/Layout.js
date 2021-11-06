import React from 'react';
import Navbar from '../components/Navbar';
import { connect } from 'react-redux';
import { checkAuthenticated, load_user } from '../actions/auth';

import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme();


const Layout = ({ checkAuthenticated, load_user, children }) => {

    return (
        <ThemeProvider theme={theme}>
            
                <Navbar />
                <div >
                    {children}
                </div>
                
            
        </ThemeProvider>
    );
};

export default connect(null, { checkAuthenticated, load_user })(Layout);
