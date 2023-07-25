#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(body);
    tasks.forEach((task) => {
      if (task.completed && dic[task.userId] === undefined) {
        dic[task.userId] = 1;
      } else if (task.completed) {
        dic[task.userId]++;
      }
    });
    console.log(dic);
  }
});
