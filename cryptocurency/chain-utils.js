const EC = require('elliptic').ec;
const SHA256 = require("crypto-js/sha256");
const { v1: uuidv1 } = require('uuid')
const ec = new EC("secp256k1");

class ChainUtil{
    static getKeyPair() {
        return ec.genKeyPair();
    }

    static id() {
        return uuidv1();
    }

    static hash(data) {
        return SHA256(JSON.stringify(data)).toString()
    }

    static verifySignature(publickey, signature, dataHash) {
        return ec.keyFromPublic(publickey,'hex').verify(dataHash,signature)
    }
}

module.exports = ChainUtil;