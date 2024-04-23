#!/usr/bin/node
// This script gets contents of webpage and stores in file

const request = require('request');
const wr_file = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    wr_file.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
