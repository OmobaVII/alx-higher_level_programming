#!/usr/bin/node
// Prints two arguments passed to it separated by is

const { argv } = require('process');
console.log(argv[2] + ' is ' + argv[3]);
