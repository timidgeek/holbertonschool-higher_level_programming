#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    console.log(`${filePath}`);
  });
});
