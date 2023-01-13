const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');

const PORT = 8000
const app = express();

app.use(helmet());
app.use(bodyParser.json());
app.use(cors());
app.use(morgan('combined'));

app.get('/', (req, res) => {
    res.send({
        good: "job"
    });
});

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});