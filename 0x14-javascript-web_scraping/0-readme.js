#!/usr/bin/node
/* A script that reads and prints the content of a file. */

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
