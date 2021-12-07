const Wallet = require("./index");
const TransactionPool = require("./transaction-pool");

describe("Wallet", () => {
  let wallet, tp;

  beforeEach(() => {
    wallet = new Wallet();
    tp = new TransactionPool();
  });

  describe("buat transaction", () => {
    let transaction, send_amount, penerima;

    beforeEach(() => {
      send_amount = 34;
      penerima = "prio_dapet";
      transaction = wallet.createTransaction(penerima, send_amount, tp);
    });

    describe("and doing the same transaction", () => {
      beforeEach(() => {
        wallet.createTransaction(penerima, send_amount, tp);
      });

      it("double the send_amount subtracted from the wallet balance", () => {
        expect(
          transaction.outputs.find(
            (output) => output.address === wallet.publickey
          ).amount
        ).toEqual(wallet.balance - send_amount * 2);
      });
    });
  });
});
