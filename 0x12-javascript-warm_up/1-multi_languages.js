#!/usr/bin/node
/**
 * This script prints 3 lines:
 * "C is fun", "Python is cool", "JavaScript is amazing"
 */
let a = 0;
const line = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

while (a < line.length) {
  console.log(line[a]);
  a++;
}
