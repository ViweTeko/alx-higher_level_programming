#!/usr/bin/node
/**
 * This script prints 'C is fun' x amount of times
 */
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  for (let a = 0; a < process.argv[2]; a++) {
    console.log('C is fun');
  }
}
