#!/usr/bin/node
const arg = process.argv[2];
const log = (arg) => console.log(arg);
let str = 'My number:';
let num = parseInt(arg);

if (isNaN(num)) {
  log('Not a number');
} else {
  log(`${str} ${num}`);
}
