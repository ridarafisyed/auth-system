import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { reset_password_confirm } from '../actions/auth';

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

const ResetPasswordConfirm = ({ match, reset_password_confirm }) => {
    const [requestSent, setRequestSent] = useState(false);
    const [formData, setFormData] = useState({
        new_password: '',
        re_new_password: ''
    });

    const { new_password, re_new_password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();

        const uid = match.params.uid;
        const token = match.params.token;

        reset_password_confirm(uid, token, new_password, re_new_password);
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
                  Set New Password
                </Typography>
                    <Box component="form" Validate sx={{ mt: 1 }} onSubmit={e => onSubmit(e)}>
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="new_password"
                            label="Password"
                            type="password"
                            value={new_password}
                            onChange={e => onChange(e)}
                            id="new_password"
                            minLength='6'
                            autoComplete="new_password"
                        />
                          <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="re_new_password"
                            label="Confirem Password"
                            type="password"
                            value={re_new_password}
                            onChange={e => onChange(e)}
                            id="re_new_password"
                            minLength='6'
                            autoComplete="re_new_password"
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
                          
                </Box>
                </Grid>
        </Grid>
        );
   
};

export default connect(null, { reset_password_confirm })(ResetPasswordConfirm);
