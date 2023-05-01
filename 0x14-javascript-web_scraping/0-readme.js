#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const log = (arg) => console.log(arg);

if (process.argv.length === 3) {
  fs.readFile(file, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    log(data);
  });
}
