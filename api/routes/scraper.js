const express = require('express');
const router = express.Router();

router.post('/add', async function (req, res) {
    res.sendStatus(200);
});

module.exports = router;