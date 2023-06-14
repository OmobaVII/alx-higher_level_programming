#!/usr/bin/node
// A script that concats 2 files

const { argv } = require('process');
const fs = require('fs');
const file1Content = fs.readFileSync(argv[2]);
const file2Content = fs.readFileSync(argv[3]);
const concatContent = file1Content + file2Content;
fs.writeFileSync(argv[4], concatContent);
