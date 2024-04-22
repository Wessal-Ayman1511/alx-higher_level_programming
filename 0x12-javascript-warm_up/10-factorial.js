#!/usr/bin/node

function factorial (x) {
  if (x === 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
const var1 = parseInt(process.argv[2]);
if (Number.isNaN(var1)) {
  console.log(1);
} else {
  console.log(factorial(var1));
}
