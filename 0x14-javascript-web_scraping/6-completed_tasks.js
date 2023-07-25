#!/usr/bin/node
// Computes the number of tasks completed by user id

const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
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
  }
});
