const express = require("express");
const bodyParser = require("body-parser");
const Blockchain = require('../blockchain/blockchain')
const P2pServer = require('./p2p-server');

const TCP_PORT = process.env.TCP_PORT || 8080;

const app = express();
const bc = new Blockchain();
const p2p = new P2pServer(bc);


// Support request with application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended: false}));
// Support request with json format
app.use(bodyParser.json())


// Getting Block
app.get('/block', (req,res) => {
    res.status(200).json(bc.chain)
})


// Mine Block
app.post('/mining', (req, res) => {
    const data = {
        amount: parseFloat(req.body.amount),
        from: req.body.from,
        to: req.body.to
    };
    const block = bc.addBlock(data);

    p2p.syncChain();

    res.redirect('/block');
})


app.listen(TCP_PORT, () => { console.log(`Server listening on port ${TCP_PORT}`); })
p2p.listen()