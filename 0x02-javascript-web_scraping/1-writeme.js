#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 4) { /* check if user has provided enough arguments (via command line ) */
  console.error('err');
} else {
  const filePath = process.argv[2];
  const stringToWrite = process.argv[3];
  fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}
