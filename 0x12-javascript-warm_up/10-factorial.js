#!/usr/bin/node
const log = (arg) => console.log(arg);
const arg = parseInt(process.argv[2]);

function factorial (num) {
  if (num < 2) {
    return 0;
  }

  return num * factorial(num - 1);
}

log(arg === 'undefined' ? 1 : factorial(arg))
