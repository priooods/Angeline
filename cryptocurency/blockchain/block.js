const ChainUtil = require("../chain-utils");
const { DIFFICULTY, MIN_RATE } = require('../config');

class Block {
  constructor(timestamp, prevhash, hash, nonce, difficulty, data) {
    this.timestamp = timestamp;
    this.prevhash = prevhash;
    this.hash = hash;
    this.nonce = nonce;
    this.data = data;
    this.difficulty = difficulty || DIFFICULTY;
  }

  toString() {
    return `Block => 
                prevhash    : ${this.prevhash}
                hash        : ${this.hash}
                timestamp   : ${this.timestamp}
                nonce       : ${this.nonce}
                difficulty  : ${this.difficulty}
                data        : ${this.data}`;
  }

  static genesis() {
    return new this("12/11/1111", "scnjddc", "cnjds", 0, DIFFICULTY,[]);
  }

  static mineBlock(lastblock, data) {
    let hash, timestamp;
    const prevhash = lastblock.hash;
    let { difficulty } = lastblock;
    let nonce = 0;

    do {
      nonce++;
      timestamp = Date.now();
      difficulty = Block.adjustDifficulty(lastblock, timestamp);
      hash = Block.hash(timestamp, prevhash, nonce, difficulty, data);
    } while (hash.substring(0, difficulty) !== "0".repeat(difficulty));

    return new this(timestamp, prevhash, hash, nonce, difficulty, data);
  }

  static hash(timestamp, prevhash, nonce, difficulty, data) {
    return ChainUtil.hash(
      `${timestamp}${prevhash}${nonce}${difficulty}${data}`
    ).toString();
  }

  static blockhash(block) {
    const { timestamp, prevhash, nonce, difficulty, data } = block;
    return Block.hash(timestamp, prevhash, nonce, difficulty, data);
  }

  static adjustDifficulty(lashblock, current_time) {
    let { difficulty } = lashblock;
    difficulty = lashblock.timestamp + MIN_RATE > current_time ? difficulty + 1 : difficulty - 1;
    return difficulty;
  };
}

module.exports = Block;