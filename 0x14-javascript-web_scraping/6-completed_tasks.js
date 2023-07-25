#!/usr/bin/node
// Computes the number of tasks completed by user id

const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const output = {};
    const result = JSON.parse(body);
    for (const a in result) {
      const data = result[a]
      if (data.completed === 'true') {
        if (output[data.userId] === undefined) {
          output[data.userId] = 1;
        } else {
          output[data.userId]++;
        }
      }
    }
    console.log(output);
  } else {
    console.log('Error code:', response.statusCode);
  }
});
