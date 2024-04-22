#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const mylist = process.argv.sort();
  console.log(mylist.reverse()[1]);
}
