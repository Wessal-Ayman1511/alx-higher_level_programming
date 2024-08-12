#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  let c = 0;
  if (!err) {
    const films = JSON.parse(body).results;

    films.forEach(film => {
        film.characters.forEach(ch_url => {
            if (ch_url.endsWith(`/18/`))
                c++;

        })
        
    });
  }
  console.log(c);
});
