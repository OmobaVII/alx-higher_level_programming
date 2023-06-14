#!/usr/bin/node
// A script that imports an array and computes a new array

const list = require('./100-data').list;
const listNow = list.map((x, index) => x * index);
console.log(list);
console.log(listNow);
