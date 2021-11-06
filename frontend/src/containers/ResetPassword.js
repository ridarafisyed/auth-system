import React, { useState } from 'react';
import {Link,  Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { reset_password } from '../actions/auth';


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

import BackgroundImage from '../asserts/login_light.png'

const ResetPassword = ({ reset_password }) => {
    const [requestSent, setRequestSent] = useState(false);
    const [formData, setFormData] = useState({
        email: ''
    });

    const { email } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();

        reset_password(email);
        setRequestSent(true);
    };

    if (requestSent) {
        return <Redirect to='/' />
    }
    return (
        <Grid container component="main" sx={{ height: '87vh' }}>
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
                Request Password Reset
                </Typography>
                    <Box component="form" Validate sx={{ mt: 1 }} onSubmit={e => onSubmit(e)}>
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            value={email}
                            onChange={e => onChange(e)}
                            autoComplete="email"
                            autoFocus
                        />
                         
                         <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                        >
                            Reset Password
                        </Button>
                    </Box>
                    <Grid container>
                    <Grid item xs>
                    <Link to="/reset-password" variant="body2">
                         {"Already have an account? Sign In"}
                    </Link>
                    </Grid>
                    <Grid item>
                    <Link to="/signup" variant="body2">
                        {"Don't have an account? Sign Up"}
                    </Link>
                    </Grid>
                </Grid>          
                </Box>
                </Grid>
        </Grid>
        );
};

export default connect(null, { reset_password })(ResetPassword);
