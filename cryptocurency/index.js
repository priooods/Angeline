// const dgram = require('dgram');

// const server = dgram.createSocket("udp4");

// server.on("error", (err) => {
//   console.log(`server error:\n${err.stack}`);
//   server.close();
// });

// server.on("message", (msg, rinfo) => {
//   console.log(`dari server lain : ${msg}`);
// });

// server.on("listening", () => {
//   const address = server.address();
//   console.log(`server listening ${address.address}:${address.port}`);
// });

// server.bind(2312);