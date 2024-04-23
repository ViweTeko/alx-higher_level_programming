#!/usr/bin/node
// This script computes number of tasks completed by user id

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const Complete = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!Complete[todo.userId]) {
        Complete[todo.userId] = 1;
      } else {
        Complete[todo.userId] += 1;
      }
    }
  });
  console.log(Complete);
});
