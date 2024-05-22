#!/usr/bin/env node

const request = require('request');

if (process.argv.length !== 3) {
    console.log("Usage: ./0-starwars_characters.js <Movie ID>");
    process.exit(1);
}

const movieId = process.argv[2];

if (isNaN(movieId)) {
    console.log("Movie ID must be a number");
    process.exit(1);
}

const fetchMovieCharacters = (movieId) => {
    const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

    request(url, { json: true }, (err, res, body) => {
        if (err) {
            console.error(`HTTP Request failed: ${err}`);
            process.exit(1);
        }
        
        if (res.statusCode !== 200) {
            console.error(`Failed to fetch data. Status code: ${res.statusCode}`);
            process.exit(1);
        }

        const characters = body.characters;

        characters.forEach((characterUrl) => {
            request(characterUrl, { json: true }, (err, res, body) => {
                if (err) {
                    console.error(`HTTP Request failed: ${err}`);
                    process.exit(1);
                }

                if (res.statusCode !== 200) {
                    console.error(`Failed to fetch data. Status code: ${res.statusCode}`);
                    process.exit(1);
                }

                console.log(body.name);
            });
        });
    });
};

fetchMovieCharacters(movieId);
