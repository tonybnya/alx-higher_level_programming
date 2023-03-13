#!/usr/bin/node
const log = (arg) => console.log(arg);

function add(a, b) {
  return (a === 'undefined' || b === 'undefined' ? NaN : a + b);
}
