#!/usr/bin/node
const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
