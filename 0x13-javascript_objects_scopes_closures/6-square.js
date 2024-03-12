#!/usr/bin/node
/* This script defines a square and inherits from 5-square.js */
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let a = 0; a < this.height;a++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
