#!/usr/bin/node
const args = process.argv;
const log = (arg) => console.log(arg);

if (typeof args[2] === 'undefined') {
  log('No argument');
} else {
  log(args[2]);
}
