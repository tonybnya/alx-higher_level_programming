#!/usr/bin/node
const args = process.argv.length;
let str = 'Argument';

if (args === 2) {
  console.log('No argument');
} else {
  args === 3 ? console.log(`${str} found`) : console.log(`${str}s found`);
}
