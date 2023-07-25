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
    for (const task in tasks) {
      if (task.completed) {
        if (dic[task.userId] === undefined) {
          dic[tasks.userId] = 1;
        } else {
          dic[tasks.userId]++;
        }
      }
    }
    console.log(dic);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
