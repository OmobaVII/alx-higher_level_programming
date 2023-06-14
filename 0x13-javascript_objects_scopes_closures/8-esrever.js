#!/usr/bin/node
// A function that returns the reversed version of a list

exports.esrever = function (list) {
  let num = 0;
  let last = list.length - 1;
  let tmp;
  while (num < last) {
    tmp = list[num];
    list[num] = list[last];
    list[last] = tmp;
    num++;
    last--;
  }
  return (list);
};
