#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer

const { argv } = require('process');
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
