const Blockchain = require("./blockchain")
const Block = require("./block")


describe("Blockchain", () => {
    let bc,bc2;

    beforeEach(() => {
        bc = new Blockchain();
        bc2 = new Blockchain();
    })

    // Testing untuk Block

    it("start with genesis block", () => {
        expect(bc.chain[0]).toEqual(Block.genesis());
    });

    it("add new block", () => {
        const data = "foo";
        bc.addBlock(data);

        expect(bc.chain[bc.chain.length - 1].data).toEqual(data);
    })

    // Testing validation chain

    it("validate a valid chain", () => {
        bc2.addBlock("data kedua");

        expect(bc.isValidChain(bc2.chain)).toBe(true);
        // output hash antar block n dan n+1 sesuai
    })

    it("validate a invalid chain", () => {
      bc2.chain[0].data = "data awal dirubah";

      expect(bc.isValidChain(bc2.chain)).toBe(false);
        // output hash antar block n dan n+1 dibuat tidak sesuai & dinyatakan chain tidak valid
        // kesimpulan program berhasil mengetahui perbedaan hash dan di gagalkan prosesnya
    });

    it("validate a corrupt chain", () => {
        bc2.addBlock("add data")
        bc2.chain[1].data = "data terakhir dirubah";

        expect(bc.isValidChain(bc2.chain)).toBe(false);
        // output hash antar block n dan n+1 dibuat tidak sesuai & dinyatakan chain tidak valid
        // kesimpulan program berhasil mengetahui perbedaan hash dan di gagalkan prosesnya
    });


    // Testing replace chain

    it("replace chain with a valid chain", () => {
      bc2.addBlock("data baru");
      bc.replaceChain(bc2.chain)

      expect(bc.chain).toEqual(bc2.chain);
      // output chain antara server pada jaringan berhasil di replace
    });

    it("replace chain with a valid chain", () => {
      bc.addBlock("data baru");
      bc.replaceChain(bc2.chain);

      expect(bc.chain).not.toEqual(bc2.chain);
      // output chain antara server pada jaringan berhasil di replace
    });
})