#!/usr/bin/node
const request = require('request'); /* import request module to make HTTP requests */

if (process.argv.length < 2) {
  console.error('URL missing');
  process.exit(1);
}

const url = process.argv[2]; /* retrieve url from user / command line */

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
