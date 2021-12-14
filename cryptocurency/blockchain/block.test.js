const Block = require('./block');
const { DIFFICULTY } = require("../config");

describe('Block', () => {
    let data, lashblock, block;
    beforeEach(() => {
        data = "ini data masukan";
        lashblock = Block.genesis();
        block = Block.mineBlock(lashblock, data);

    })
    it("set block `data` to match input ", () => {
        expect(block.data).toEqual(data)
    });
    

    it("set `prevhash` to match hash of the lasthash", () => {
      expect(block.prevhash).toEqual(lashblock.hash);
    });

    it("hash yang dibuat berdasarkan kesulitan", () => {
      expect(block.hash.substring(0, block.difficulty)).toEqual(
        "0".repeat(block.difficulty)
      );
    });

    it("lower difficulty for slowly mine block", () => {
      expect(Block.adjustDifficulty(block, block.timestamp + 360000)).toEqual(
        block.difficulty - 1
      );
    });

    it("raises the difficulty for quickly mine block", () => {
      expect(Block.adjustDifficulty(block, block.timestamp + 1)).toEqual(
        block.difficulty + 1
      );
    });
})