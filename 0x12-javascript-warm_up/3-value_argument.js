#!/usr/bin/node
/**
 * This script prints the first arguments passed to it
 * or 'No argument' if there are none
 */
!process.argv[2]
  ? console.log('No argument')
  : console.log(process.argv[2]);
