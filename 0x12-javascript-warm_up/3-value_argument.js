#!/usr/bin/node
const args = process.argv;
const log = (arg) => console.log(arg);

if (!args[2]) {
  log('No argument');
} else {
  log(args[2]);
}
