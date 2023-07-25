#!/usr/bin/node
// Computes the number of tasks completed by user id

const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const output = {};
    const data = JSON.parse(body);
    for (const a in data) {
      if (data[a].completed) {
        if (output[data[a].userId] === undefined) {
          output[data[a].userId] = 1;
        } else {
          output[data[a].userId] += 1;
        }
      }
    }
    console.log(output);
  } else {
    console.log('Error code:', response.statusCode);
  }
});
