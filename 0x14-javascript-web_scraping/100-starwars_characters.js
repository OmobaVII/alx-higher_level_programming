#!/usr/bin/node
// Prints all character of A star wars movie

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const characterurl of characters) {
      request(characterurl, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
