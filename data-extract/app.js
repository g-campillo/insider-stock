var express = require('express');
var app = express();
const axios = require('axios');

const PORT = process.env.PORT;

app.get('/home', (req, res) => {
    axios.get(`${process.env.API_URL}/?page=0&apikey=${process.env.API_KEY}`)
    .then(res => {
        console.log(JSON.stringify(res));
    })
    .catch(err => {
        console.log('There was an error making the request');
    });
});

app.listen(PORT, () => {
    console.log('running on port 3000');
});