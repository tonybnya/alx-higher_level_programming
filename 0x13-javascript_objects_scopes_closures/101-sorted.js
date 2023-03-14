#!/usr/bin/node
const { dict } = require('./101-data').dict;
let result = {};

for (const key in dict) {
  const occurrences = dict[key];

  if (!result[occurrences]) {
    result[occurrences] = [];
  }
  result[occurrences].push(key);
}

console.log(result);
