#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    for (const film of films) {
      const filmChars = film.characters;

      for (const characterURL of filmChars) {
        if (characterURL.includes('18')) {
          count++;
        }
      }
    }

    console.log(count);
  } else {
    console.log('An error occurred. Status code:', response.statusCode);
  }
});
