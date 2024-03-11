#!/usr/bin/node
/**
 * This script prints 'My number: <first arg converted to int>'
 */
const num = parseInt(process.argv[2]);

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
