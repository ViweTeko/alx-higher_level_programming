#!/usr/bin/node
/**
 * This script prints a message dependent on
 * the number of arguments passed
 */
process.argv.length < 3
  ? console.log('No argument')
  : process.argv.length === 3
    ? console.log('Argument found')
    : console.log('Arguments found');
