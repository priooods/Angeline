const Transaction = require('./transaction');
const Wallet = require('./index');

describe('Transaction', () => {
    let transaction, wallet, penerima, amount;

    beforeEach(() => {
        wallet = new Wallet();
        amount = 30;
        penerima = "bdasjidjwi";
        transaction = Transaction.newTransaction(wallet, penerima, amount);
    })

    it('input amount harus mengurangi uang yang dipunya pengirim', () => {
        expect(
          transaction.outputs.find((output) => output.address === wallet.publickey)
            .amount
        ).toEqual(wallet.balance - amount);
    })

    it("output amount diterima user tujuan", () => {
      expect(
        transaction.outputs.find(
          (output) => output.address === penerima
        ).amount
      ).toEqual(amount);
    });

    it("tambahin saldo ke wallet", () => {
      expect(
        transaction.input.amount
      ).toEqual(wallet.balance);
    });

    it("verifikasi , transaksi = valid", () => {
      expect(Transaction.verifyTransaction(transaction)).toBe(true);
    });

    it("verifikasi , transaksi = invalid", () => {
        transaction.outputs[0].amount = 5000000;
      expect(Transaction.verifyTransaction(transaction)).toBe(false);
    });

    describe('Transaksi uang melebihi saldo di wallet', () => {
        beforeEach(() => {
            amount = 5000000;
            transaction = Transaction.newTransaction(wallet, penerima, amount);
        });

        it('gagal membuat transaksi', () => {
            expect(transaction).toEqual(undefined);
        });
    })

    describe("an update Transaksi", () => {
        let amount_in, next_penerima;
        beforeEach(() => {
            amount_in = 123;
            next_penerima = 'n3xt-4ddr335';
            transaction = transaction.update(wallet, next_penerima, amount_in);
        });

        it("kurangi jumlah berikutnya dari output pengirim", () => {
            expect(transaction.outputs.find(output => output.address === wallet.publickey).amount)
                .toEqual(wallet.balance - amount - amount_in);
        });

        it("outputs an amount for the next recipient", () => {
          expect(
            transaction.outputs.find(
              (output) => output.address === next_penerima
            ).amount
          ).toEqual(amount_in);
        });
    });

})