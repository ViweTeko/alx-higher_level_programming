#!/usr/bin/node
/* This script writes a square class and defines it,
 * while inheriting from Rectangle of 4-rectangle.js
 */
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
