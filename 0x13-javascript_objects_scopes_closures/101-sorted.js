#!/usr/bin/node
const { dict } = require('./101-data').dict;
let result = {};

for (let key in dict) {
  if (result[dict[key]] === undefined) {
    result[dict[key]] = [key];
  } else {
    result[dict[key]].push(key);
  }
}

console.log(result);
