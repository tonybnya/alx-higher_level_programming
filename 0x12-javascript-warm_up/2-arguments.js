#!/usr/bin/node
const args = process.argv.length;
const log = (arg) => console.log(arg);
let s = 'Argument';

log(args === 2 ? 'No argument' : args === 3 ? log(`${str} found`) : log(`${str}s found`));
