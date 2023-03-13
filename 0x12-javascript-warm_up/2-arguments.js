#!/usr/bin/node
import { argv } from 'node:process';

const args = argv.length;
const log = (arg) => console.log(arg);
let str = 'Argument';

if (args === 2) {
  log('No argument');
} else {
  args === 3 ? log(`${str} found`): log(`${str}s found`);
}
