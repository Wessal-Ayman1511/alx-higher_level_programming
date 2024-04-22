#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const var1 = parseInt(process.argv[2]);
const var2 = parseInt(process.argv[3]);
console.log(add(var1, var2));
