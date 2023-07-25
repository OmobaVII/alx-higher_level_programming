#!/usr/bin/node
// Prints the number of movies where the character Wedge Antilles is present

const { argv } = require('process');
const request = require('request');

let number = 0;

request(argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body).results;
    for (const movie of data) {
      if (movie.characters.includes("https://swapi-api.alx-tools.com/api/people/18/")) {
        number += 1;
      };
    }
    console.log(number);
  };
});
