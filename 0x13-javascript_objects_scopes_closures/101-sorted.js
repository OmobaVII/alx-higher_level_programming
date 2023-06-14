#!/usr/bin/node
// A script that imports a dictionary of occurences by user id

const dict = require('./101-data').dict;
const dictNow = {};
let value;
for (value in dict) {
  if (dictNow[dict[value]] === undefined) {
    dictNow[dict[value]] = [];
  }
  dictNow[dict[value]].push(value);
}
console.log(dictNow);
