#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  let count = 0;

  if (!err) {
    const films = JSON.parse(body).results;

    films.forEach(film => {
      film.characters.forEach(characterUrl => {
        if (characterUrl.endsWith('/18/')) {
          count++;
        }
      });
    });
  }

  console.log(count);
});
