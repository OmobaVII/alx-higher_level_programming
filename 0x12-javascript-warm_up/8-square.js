#!/usr/bin/node
// Script that prints a square

const { argv } = require('process');
let num1 = 0;
if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  while (num1 < parseInt(argv[2])) {
    console.log('X'.repeat(parseInt(argv[2])));
    num1++;
  }
}
