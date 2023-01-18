const mysql = require('mysql2');
require('dotenv').config();

const sqlPool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    port: process.env.DB_PORT,
    database: process.env.DATABASE,
    connectionLimit: process.env.CONNECTION_LIMIT,
    queueLimit: process.env.QUEUE_LIMIT,
    waitForConnections: process.env.WAIT_FOR_CONNECTIONS
});

const promisePool = sqlPool.promise();

async function getRecords(limit) { 
    let query = `SELECT * FROM trades LIMIT ${limit} ORDER BY tradeDate DESC, filingDate DESC`;
    let [records, fields] = await promisePool.query(query)
    return records;
}

module.exports = {
    getRecords
}