#!/usr/bin/node
/** This script prints a square
 */
if (isNaN(process.argv[2]))
	console.log('Missing size');
else {
	const size = parseInt(process.argv[2]);
	for (let a = 0; a < size; a++)
		console.log(Array(size( + 1).join('X'));
