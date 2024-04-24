#!/usr/bin/node
// This script reads from file

const rd_file = require('fs');
rd_file.readFile(process.argv[2],'utf-8',
  function (error, data) {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });
