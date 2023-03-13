#!/usr/bin/node
const log = (arg) => console.log(arg);
const arg = parseInt(process.argv[2]);

function factorial (num) {
  if (num < 1) {
    return 0;
  }

  return factorial(num) * factorial(num - 1);
}

log(arg === 'undefined' ? 1 : factorial(arg))