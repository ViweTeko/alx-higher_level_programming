#!/usr/bin/node
/* This script prints number of arguments already printed along with new argument*/
let countLog = 0;
exports.logMe = (item) => {
  console.log(`${countLog}: ${item}`);
  countLog++;
};
