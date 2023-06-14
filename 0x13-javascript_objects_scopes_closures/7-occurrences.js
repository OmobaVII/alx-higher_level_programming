#!/usr/bin/node
// A function that returns the number of occurrents in a list

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  let occurence = 0;
  while (num < list.length) {
    if (list[num] === searchElement) {
      occurence++;
    }
    num++;
  }
  return (occurence);
};
