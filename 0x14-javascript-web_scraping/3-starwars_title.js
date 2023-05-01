#!/usr/bin/node
// This JS script prints the title of a Star Wars movie
// where the episode number matches a given integer.

const req = require('request');
const log = (arg) => console.log(arg);
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/:'
const endpoint = `${url}+${id}`;

log(endpoint);
