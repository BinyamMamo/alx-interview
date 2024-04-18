#!/usr/bin/node

let request = require("request");

url = "https://swapi-api.alx-tools.com/api/";
end_point = `films/${process.argv[2]}`;

function request_api(url) {
    return new Promise((resolve, reject) => {
        request(url, (err, resp, body) => {
            if (err) reject(err);
            resolve(JSON.parse(body));
        })
    });
}

request_api(url + end_point)
    .then(film => film.characters)
    .then(characters => Promise.all(characters.map(character => request_api(character))))
    .then(characters => characters.map(character => console.log(character.name)))
    .catch(error => console.error(error))
