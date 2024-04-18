#!/usr/bin/node

let request = require("request");

url = "https://swapi-api.alx-tools.com/api/";
end_point = `films/${process.argv[2]}`;
console.log(request(url + end_point));
