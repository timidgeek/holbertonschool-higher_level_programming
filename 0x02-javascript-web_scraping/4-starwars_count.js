#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const films = JSON.parse(body).results;
  const numWedgeMovies = films.filter(film => {
    const characters = film.characters;
    return characters.some(character => character.endsWith(`/${characterId}/`));
  }).length;
  console.log(`${numWedgeMovies}`);
});
