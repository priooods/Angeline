const Websocket = require('ws');
const MESSAGE_TYPE = {
  chain: "CHAIN",
  transaction: "TRANSACTION ",
};

const P2P_PORT = process.env.P2P_PORT || 5001;
const peers = process.env.PEERS ? process.env.PEERS.split(",") : [];

class P2pServer {
  constructor(blockchain, transactionPool) {
    this.blockchain = blockchain;
    this.transactionPool = transactionPool;
    this.socket = [];
  }

  listen() {
    const server = new Websocket.Server({ port: P2P_PORT });
    server.on("connection", (socket) => this.connectSocket(socket));

    this.connectToPeers();

    console.log(`listening peer to peer connection in ${P2P_PORT}`);
  }

  connectToPeers() {
    peers.forEach((peer) => {
      const sock = new Websocket(peer);
      sock.on("open", () => this.connectSocket(sock));
    });
  }

  connectSocket(socket) {
    this.socket.push(socket);
    console.log("socket connected ");

    this.messageHandler(socket);

    this.sendChain(socket);
  }

  messageHandler(socket) {
    socket.on("message", (message) => {
      const data = JSON.parse(message);
      // console.log(`block ${P2P_PORT}`, data);
      // console.log(`list PEERS `, peers);

      switch (data.type) {
        case MESSAGE_TYPE.chain:
          this.blockchain.replaceChain(data);
          break;
        case MESSAGE_TYPE.transaction:
          this.transactionPool.updateOrAddTransaction(data.transaction);
          break;
      }
    });
  }

  sendChain(socket) {
    socket.send(
      JSON.stringify({ type: MESSAGE_TYPE.chain, chain: this.blockchain.chain })
    );
  }

  syncChain() {
    this.socket.forEach((socket) => {
      this.sendChain(socket);
    });
  }

  sendTransaction(socket, transaction) {
    socket.send(
      JSON.stringify({ type: MESSAGE_TYPE.transaction, transaction })
    );
  }

  broadcastTransaction(transaction) {
    this.socket.forEach((socket) => this.sendTransaction(socket, transaction));
  }
}

module.exports = P2pServer;