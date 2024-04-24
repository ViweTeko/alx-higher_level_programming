#!/usr/bin/node
// This script writes a string to a file

const wr_file = require('fs');

wr_file.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (error) {
    if (error) {
      console.log(error);
    }
  });
