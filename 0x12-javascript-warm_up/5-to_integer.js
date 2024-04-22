#!/usr/bin/node
const var1 = parseInt(process.argv[2]);
if (Number.isNaN(var1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + var1);
}
