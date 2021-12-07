// const dgram = require("dgram");
// const { Buffer } = require("buffer");

// const message = Buffer.from("Hallo harbi bangsat !!");
// const client = dgram.createSocket("udp4");
// client.send(message, 2312, "172.16.11.180", (err) => {
//   client.close();
// });
const Blockchain = require('./blockchain/blockchain');
const Wallet = require('./wallet/index')
const Transaction = require("./wallet/transaction");
const wallet = new Wallet();
const ChainUtil = require('./chain-utils')
console.log(wallet.toString());
// console.log(ChainUtil.id());

const test = Transaction.newTransaction(wallet, ChainUtil.id(), 50);
console.log(test);

// const bc = new Blockchain();

// for (let index = 0; index < 15; index++) {
//     console.log(bc.addBlock(` data ke ${index}`).toString());
// }