#!/usr/bin/node
const { dict } = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  const occurrences = dict[key];

  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(key);
}

console.log(newDict);
