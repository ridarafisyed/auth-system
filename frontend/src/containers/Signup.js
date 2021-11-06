import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { signup } from '../actions/auth';

import {
    Avatar,
    Button, 
    Paper,
    Grid,
    Box,
    Typography,
    TextField,

} from '@mui/material';

import LockOutlinedIcon from '@mui/icons-material/LockOutlined';

import BackgroundImage from '../asserts/signup_light.png'


const Signup = ({ signup, isAuthenticated }) => {
    const [accountCreated, setAccountCreated] = useState(false);
    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        re_password: ''
    });

    const {email, first_name, last_name,  password, re_password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();

        if (password === re_password) {
            signup(email, first_name, last_name,  password, re_password);
            setAccountCreated(true);
        }
    };

    if (isAuthenticated) {
      return <Redirect to='/' />
  }
  if (accountCreated) {
      return <Redirect to='/login' />
  }


    return (
        <Grid container component="main" sx={{ height: '85vh' }}>
        <Grid
          item
          xs={false}
          sm={4}
          md={8}
          sx={{
            backgroundImage: `url(${BackgroundImage})`,
            backgroundRepeat: 'no-repeat',
            backgroundColor: (t) =>
              t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        />
          <Grid item xs={12} sm={8} md={4} component={Paper} elevation={6} square>
          <Box
            sx={{
              my: 8,
              mx: 4,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >   
            <Avatar sx={{ m: 1, bgcolor: 'warning.main' }}>
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign in
            </Typography>
                <Box component="form" Validate sx={{ mt: 1 }}onSubmit={e => onSubmit(e)}>
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={6}>
                    <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="first_name"
                            label="First Name"
                            name="first_name"
                            value={first_name}
                            onChange={e => onChange(e)}
                            autoComplete="first_name"
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={12} sm={6}>
                    <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="last_name"
                            label="Last Name"
                            name="last_name"
                            autoComplete="last_name"
                            value={last_name}
                            onChange={e => onChange(e)}
                            autoFocus
                        />
                        </Grid>
                    </Grid>
                    <Grid item xs={12} >
                    <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            value={email}
                            onChange={e => onChange(e)}
                            autoFocus
                        />
                        </Grid>
                        <Grid item xs={12} >
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        autoComplete="password"
                        value={password}
                        onChange={e => onChange(e)}
                    />
                    </Grid>
                    <Grid item xs={12}>
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        name="re_password"
                        label="Confirm Password"
                        type="password"
                        value={re_password}
                        onChange={e => onChange(e)}
                        id="re_password"
                        autoComplete="re_password"
                    /></Grid>
                  
                    <Button type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}>Register</Button>
            </Box>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link to='/login' variant="body2">
                 {"Already have an account? Sign in"}
                </Link>
              </Grid>
            </Grid>
            
        </Box>
        </Grid></Grid>
    );
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { signup })(Signup);
