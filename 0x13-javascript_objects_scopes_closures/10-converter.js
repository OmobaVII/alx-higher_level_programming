#!/usr/bin/node
// a function that converts a number from base 10 to another base passed as an argument

exports.converter = function (base) {
  function conv (num) {
    return (num.toString(base));
  }
  return (conv);
};
