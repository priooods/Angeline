const { INITIAL_BALANCE } = require("../config");
const ChainUtil = require("../chain-utils");
const Transaction = require("./transaction");

class Wallet {
  constructor() {
    this.balance = INITIAL_BALANCE;
    this.keyPair = ChainUtil.getKeyPair();
    this.publickey = this.keyPair.getPublic().encode("hex");
  }

  toString() {
    return `Wallet => 
            publickey   : ${this.publickey}
            balance     : ${this.balance}`;
  }

  sign(data_hash) {
    return this.keyPair.sign(data_hash);
  }

  createTransaction(penerima, amount, transactionPool) {
    if (amount > this.balance) {
      console.log(
        `Amount : ${amount} exceceds current balance: ${this.balance}`
      );
      return;
    }

    let transaction = transactionPool.existingTransaction(this.publickey);
    if (transaction) transaction.update(this, penerima, amount);
    else {
      transaction = Transaction.newTransaction(this, penerima, amount);
      transactionPool.updateOrAddTransaction(transaction);
    }

    return transaction;
  }
}

module.exports = Wallet;
