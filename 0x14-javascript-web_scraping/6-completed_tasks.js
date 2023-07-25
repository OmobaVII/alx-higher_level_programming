#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        if (dic[task.userId] === undefined) {
          dic[task.userId] = 1;
        } else {
          dic[task.userId]++;
        }
      }
    }
    console.log(dic);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
