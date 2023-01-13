const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const db = require('./helpers/database');
require('dotenv').config();

const PORT = 8000;
const app = express();

app.use(helmet());
app.use(bodyParser.json());
app.use(cors());
app.use(morgan('combined'));



// GET Methods

// Gets records from trades table
app.get('/records', async function (req, res) {
    let records = await db.getRecords(req.query.limit || 100);
    res.send(records);
});

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});