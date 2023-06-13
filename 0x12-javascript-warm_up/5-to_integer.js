#!/usr/bin/node
// Prints My number: first argument converted in integer

const { argv } = require('process');
if (isNaN(parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(argv[2]));
}
