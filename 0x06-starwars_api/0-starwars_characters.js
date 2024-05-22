#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

if (isNaN(movieId)) {
  console.log('Movie ID must be a number');
  process.exit(1);
}

const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(movieUrl, { json: true }, (err, res, body) => {
  if (err || res.statusCode !== 200) {
    console.error(`Failed to fetch data: ${err || `Status code ${res.statusCode}`}`);
    process.exit(1);
  }

  const characters = body.characters;
  const characterNames = Array(characters.length).fill(null);

  let completedRequests = 0;

  characters.forEach((url, index) => {
    request(url, { json: true }, (err, res, body) => {
      if (!err && res.statusCode === 200) {
        characterNames[index] = body.name;
      }
      completedRequests++;
      if (completedRequests === characters.length) {
        characterNames.forEach(name => console.log(name));
      }
    });
  });
});
