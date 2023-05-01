#!/usr/bin/node
// This JS script prints all characters of a Star Wars movie.

const log = (arg) => console.log(arg);
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const endpoint = `${url}${id}`;

req.get(endpoint, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const data = JSON.parse(body);
  const chars = data.characters;

  for (const char of chars) {
    req.get(char, (err, res, body) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }

      const data = JSON.parse(body);
      log(data.name);
    });
  }
});
