#!/usr/bin/node
const args = process.argv;
const log = (arg) => console.log(arg);

log(typeof args[2] === 'undefined' ? 'No argument' : args[2]);
