#!/usr/bin/node
// Displays the status code of a GET request

const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, response) {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
