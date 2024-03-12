#!/usr/bin/node
/* This script expands futher the Rectangle class with added methods */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /* This method prints the rectangle */
  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }

  /* This method exchanges width and height values */
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  /* This method doubles the width and height */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
