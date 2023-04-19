#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

if (process.argv.length < 4) {
  console.error('not enough arguments');
} else {
  request.get(url, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
}
