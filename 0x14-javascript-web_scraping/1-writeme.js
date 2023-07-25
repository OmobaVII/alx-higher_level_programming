#!/usr/bin/node
// Writes a string to a file

const { argv } = require('process');
const fs = require('fs');

fs.writeFile(argv[2], argv[3], 'utf8', function (err) {
  if (err) {
    console.error(err);
  }
});
