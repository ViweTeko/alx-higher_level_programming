#!/usr/bin/node
/* This script prints a factorial */
function factorial (a) {
	if (a > 0)
		return (a * factorial(a - 1));
	else
		return 1;
}
const res = parseInt(process.argv[2]);
console.log(factorial(res);
