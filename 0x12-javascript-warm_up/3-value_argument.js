#!/usr/bin/node
// Prints the first argument passed to it

const { argv } = require('process');

if (typeof (argv[2]) === 'undefined') {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
