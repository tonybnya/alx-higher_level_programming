#!/usr/bin/node
const log = (arg) => console.log(arg);

function add(a, b) {
  log(a === 'undefined' || b === 'undefined' ? NaN : a + b);
}
