#!/usr/bin/node
// defines a class Square that inherits from Square of 5-square.js

const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let num = 0;
      while (num < this.width) {
        console.log(c.repeat(this.width));
        num++;
      }
    }
  }
}
module.exports = Square;
