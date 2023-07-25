#!/usr/bin/node
// Computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(body);
    for (const a in tasks) {
      if (tasks[a].completed) {
        if (dic[tasks[a].userId] === undefined) {
          dic[tasks[a].userId] = 1;
        } else {
          dic[tasks[a].userId]++;
        }
      }
    }
    console.log(dic);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
