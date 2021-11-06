
import React, { Fragment, useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth';

import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

import Logo from '../asserts/logo_white copy.png'

const Navbar = ({ logout, isAuthenticated }) => {
    const [redirect, setRedirect] = useState(false);

    const logout_user = () => {
        logout();
        setRedirect(true);
    };

    const guestLinks = () => (
        <Fragment>
            <Button component={Link} color="inherit" to='/login'>Login </Button>
            <Button  component={Link} color="inherit"to='/signup'>Sign Up</Button>
        </Fragment>
    );

    const authLinks = () => (
            <Button component={Link} color="inherit" href='#!' onClick={logout_user}>Logout</Button>
        
    );
    return (
        <Fragment>
            <Box sx={{ flexGrow: 1 }} component="nav">
            <AppBar position="static" color="transparent">
                <Toolbar>
                <IconButton
                    size="large"
                    edge="start"
                    color="inherit"
                    aria-label="menu"
                    sx={{ mr: 2 }}
                >
                    <MenuIcon />
                </IconButton>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                <Link to="/"> <img src={Logo} alt="logo" style={{height:"2rem", width:'auto'}}/></Link>
                </Typography>
                {isAuthenticated ? authLinks() : guestLinks()}
                </Toolbar>
            </AppBar>
            </Box>
            {redirect ? <Redirect to='/' /> : <Fragment></Fragment>}
    </Fragment>
  );
}
const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { logout })(Navbar);