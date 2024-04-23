#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const i in list) {
    if (searchElement === list[i]) {
      counter++;
    }
  }
  return counter;
};
