#!/usr/bin/node
// Create and instance method on the Rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let num = 0;
    while (num < this.height) {
      console.log('X'.repeat(this.width));
      num++;
    }
  }
}
module.exports = Rectangle;
