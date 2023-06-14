#!/usr/bin/node
// a function that prints the number of arguments already printes and the new argument

let num = 0;
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num++;
};
