#!/usr/bin/node
// Prints the number of movies where the character Wedge Antilles is present

const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body).results;
    let number = 0;

    for (const a in data) {
      const actors = data[a].characters;
      for (const b in actors) {
        if (actors[b].includes('18')) {
          number += 1;
        }
      }
    }
    console.log(number);
  }
});
