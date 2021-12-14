const Block = require("./block");
// const dgram = require('dgr')

class Blockchain {
    constructor() {
        this.chain = [Block.genesis()]
    }


    addBlock(data){
        // " this.chain[this.chain.length - 1] " value untuk dapetin block terakhir
        // buat obj block
        const block = Block.mineBlock(this.chain[this.chain.length - 1], data);
        // tambah obj ke jaringan blockchain
        this.chain.push(block);

        return block;
    }

    isValidChain(chain) {
        if (JSON.stringify(chain[0]) !== JSON.stringify(Block.genesis())) return false
        
        for (let i = 1; i < chain.length; i++) {
            const block = chain[i]
            const lastBlock = chain[i - 1];

            if (
              block.prevhash !== lastBlock.hash ||
              block.hash !== Block.blockhash(block)
            )
              return false;
        }
        return true;
    }

    replaceChain(newChain) {
        console.log("mereplace chain lama jadi baru");

        if (newChain.length < this.chain.length) {
            console.log("chain baru tidak sepanjang chain asli");
            return;
        } else if (!this.isValidChain(newChain)) {
            console.log("chain pada jaringan tidak valid");
            return;
        }
        this.chain = newChain
    }
}

module.exports = Blockchain