#!/usr/bin/node
// A script that searches for the second largest integer

const { argv } = require('process');
const arrArgv = argv.slice(2);
function secondBiggest (arr) {
  if (arr.length < 2) {
    return (0);
  } else {
    arr.sort((a, b) => b - a);
    // arr.sort((a, b) => a - b) sorts in ascending order
    return (arr[1]);
  }
}
console.log(secondBiggest(arrArgv));
