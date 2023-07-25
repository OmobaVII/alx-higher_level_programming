#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

function countCompletedTasksByUserId (todos) {
  const completedTasksByUserId = {};

  for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId.toString();
      completedTasksByUserId[userId] = (completedTasksByUserId[userId] || 0) + 1;
    }
  }
  return completedTasksByUserId;
}
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error fetching data:', error);
  } else if (response.statusCode !== 200) {
    console.error('API request failed:', response.statusCode);
  } else {
    try {
      const todos = JSON.parse(body);
      const completedTasksByUserId = countCompletedTasksByUserId(todos);
      console.log(completedTasksByUserId);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
