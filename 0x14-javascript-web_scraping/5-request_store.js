#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const { argv } = require('process');
const request = require('request');
const fs = require('fs');

request(argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(argv[3], body, 'utf-8', function (error) {
      if (error) {
        console.error(error);
      }
    });
  }
});
