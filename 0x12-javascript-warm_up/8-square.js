#!/usr/bin/node
/** This script prints a square
 */
const process = require('process');
const aArg = process.argv[2];
const size = parseInt(aArg);

if (!isNaN(size)) {
  if (size > 0) {
    for (let a = 0; a < size; a++) {
      let row = '';
      for (let b = 0; b < size; b++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
