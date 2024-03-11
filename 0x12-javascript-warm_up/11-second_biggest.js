#!/usr/bin/node
/**
 * This script searches the second
 * biggest integer in list of args
 */
const arglen = process.argv.length;
if (arglen <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2, arglen);
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
