#!/usr/bin/node
// a function that executes x times

let num = 0;
function callMeMoby (x, theFunction) {
  while (num < x) {
    theFunction();
    num++;
  }
}
module.exports = {
  callMeMoby
};
