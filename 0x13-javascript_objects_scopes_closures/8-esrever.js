#!/usr/bin/node
/* This script returns the reversed version of a list */
exports.esrever = (list) => {
  const newList = [];
  const len = list.length;
  for (let a = len - 1; a > 0; a--) {
    newList.push(list[a]);
  }
  return newList;
};
