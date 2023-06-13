#!/usr/bin/node
// Script that prints x times C is fun

const { argv } = require('process');
let num = 0;
if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  while (num < parseInt(argv[2])) {
    console.log('C is fun');
    num++;
  }
}
