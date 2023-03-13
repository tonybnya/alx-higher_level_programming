#!/usr/bin/node
const log = (arg) => console.log(arg);
const args = process.argv;

function secondBiggest (arr) {
  return arr[arr.length - 2];
}

if (args.length <= 3) {
  log(0);
} else {
  args.sort();
  log(secondBiggest(args));
}
