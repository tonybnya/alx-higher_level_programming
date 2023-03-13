#!/usr/bin/node
import { argv } from 'node:process';

const args = argv.length;
const log = (arg) => console.log(arg);
let str = 'Argument';

if (args === 2) {
  console.log('No argument');
} else {
  args === 3 ? console.log(`${str} found`): console.log(`${str}s found`);
}
