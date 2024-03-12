#!/usr/bin/node
/* This script converts a number from base 10 to another base */
exports.converter = (base) => {
  return (decimalNumber) => {
    return decimalNumber.toString(base);
  };
};
