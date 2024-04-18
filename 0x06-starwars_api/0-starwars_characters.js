#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/';
const endPoint = `films/${process.argv[2]}`;

function requestAPI (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, resp, body) => {
      if (err) reject(err);
      resolve(JSON.parse(body));
    });
  });
}

requestAPI(url + endPoint)
  .then(film => film.characters)
  .then(characters => Promise.all(characters.map(character => requestAPI(character))))
  .then(characters => characters.map(character => console.log(character.name)))
  .catch(error => console.error(error));
