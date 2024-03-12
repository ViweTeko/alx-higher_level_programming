#!/usr/bin/node
/* This function returns number of occurrences in a list */
exports.nbOccurences = (list, searchElement) => {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
