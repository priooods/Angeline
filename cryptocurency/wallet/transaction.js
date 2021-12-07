const ChainUtil = require('../chain-utils');

class Transaction{
  constructor() {
      this.id = ChainUtil.id();
      this.input = null;
      this.outputs = []
  }

  update(pengirim, penerima, amount) {
    const pengirim_out = this.outputs.find(output => output.address === pengirim.publickey);
    if (amount > pengirim_out.amount) {
      console.log(`Amount : ${amount} melebihi balance`);
      return;
    }

    pengirim_out.amount = pengirim_out.amount - amount;
    this.outputs.push({ amount, address: penerima });
    Transaction.signTransaction(this, pengirim);

    return this;
  }

  static newTransaction(pengirim, penerima, amount) {
      const transaction = new this();

      if (amount > pengirim.balance) {
          console.log(`Amount : ${amount} melebihi balance`);
          return;
      }

      transaction.outputs.push(
        ...[
          { amount: pengirim.balance - amount, address: pengirim.publickey },
          { amount, address: penerima },
        ]
      );
      
      Transaction.signTransaction(transaction,pengirim)

      return transaction;
  }
  
  static signTransaction(transaction, pengirim) {
    transaction.input = {
      timestamp: Date.now(),
      amount: pengirim.balance,
      address: pengirim.publickey,
      signature: pengirim.sign(ChainUtil.hash(transaction.outputs)),
    };
  }

  static verifyTransaction(transaction) {
    return ChainUtil.verifySignature(
      transaction.input.address,
      transaction.input.signature,
      ChainUtil.hash(transaction.outputs)
    )
  }
}

module.exports = Transaction