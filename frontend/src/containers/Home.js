import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => (
    <div className='container'>
        <div class='jumbotron mt-5'>
            <h1 class='display-4 mt-3'>Welcome to Dextera!</h1>
            <p class='lead'>The Law firm!</p>
            <hr class='my-4' />
            
            <Link class='btn btn-primary btn-lg' to='/login' role='button'>Login</Link>
        </div>
    </div>
);

export default Home;
