#!/usr/bin/node
// This JS script computes the number of tasks completed by user id.

const req = require('request');
const url = process.argv[2];
const completedTasks = {};
const log = (arg) => console.log(arg);

req.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const data = JSON.parse(body);

  data.forEach((user) => {
    if (!(user.userId in completedTasks)) {
      completedTasks[userId] = 1;
    } else {
      completedTasks[userId] += 1;
    }
  });

  log(completedTasks);
});
