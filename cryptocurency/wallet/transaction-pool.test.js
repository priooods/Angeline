const TransactionPool = require("./transaction-pool");
const Transaction = require("./transaction");
const Wallet = require("./index");

describe("TransactionPool", () => {
  let tp, wallet, transaction;

  beforeEach(() => {
    tp = new TransactionPool();
    wallet = new Wallet();
    transaction = Transaction.newTransaction(wallet, "prio-address", 23);
    tp.updateOrAddTransaction(transaction);
  });

  it("tambah transaction pool", () => {
    expect(tp.transaction.find((t) => t.id === transaction.id)).toEqual(
      transaction
    );
  });

  it("update transaction pool", () => {
    const old_transac = JSON.stringify(transaction);
    const new_transac = transaction.update(wallet, "prio_next_address", 1998);
    tp.updateOrAddTransaction(new_transac);
    expect(
      JSON.stringify(tp.transaction.find((t) => t?.id === new_transac?.id))
    ).not.toEqual(old_transac);
  });
});
