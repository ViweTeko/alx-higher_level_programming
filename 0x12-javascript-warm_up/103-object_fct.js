#!/usr/bin/node
/**
 * This script is updated by adding new function incr
 * that increments the integer value
 */
const myObject = {
	type: 'object',
	value: 12
};
console.log(myObject);
myObject.incr = function () {
	myObject.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObjct.incr();
console.log(myObject);
