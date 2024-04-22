#!/usr/bin/node

const args = process.argv.length;
if (args === 2) {
  console.log('No argument');
}
if (args === 3) {
  console.log('Argument found');
} 
if (args > 3)
{
  console.log('Arguments found');
}
