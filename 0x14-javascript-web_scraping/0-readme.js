#!/usr/bin/node
<<<<<<< HEAD
# This JS script reads and prints the content of a file.
=======
>>>>>>> 30d935299e6d59b7a58647935e6686c0b84063c3

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
