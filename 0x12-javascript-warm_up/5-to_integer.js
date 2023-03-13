#!/usr/bin/node
const arg = process.argv[2];
const log = (arg) => console.log(arg);
const str = 'My number:';
const parseInt = parseInt(arg);

if (isNaN(num)) {
  log('Not a number');
} else {
  log(`${str} ${num}`);
}
