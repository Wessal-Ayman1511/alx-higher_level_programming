#!/usr/bin/node
exports.esrever = function (list) {
  const temp = [];
  let x = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    temp[x++] = list[i];
  }
  return temp;
};
