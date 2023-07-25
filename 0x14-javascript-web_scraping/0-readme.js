#!/usr/bin/node
// Reads and prints the content of a file

const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2], 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
