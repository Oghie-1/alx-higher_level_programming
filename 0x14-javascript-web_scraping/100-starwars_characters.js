#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (charErr, charResponse, charBody) => {
        if (charErr) {
          console.error(charErr);
        } else if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.log('Error occurred while fetching character. Status code:', charResponse.statusCode);
        }
      });
    });
  } else {
    console.log('Error occurred while fetching movie data. Status code:', response.statusCode);
  }
});
