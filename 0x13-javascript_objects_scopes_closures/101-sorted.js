#!/usr/bin/node
/* This script imports a dictionary of occurrences
 * by user id and computes dictionary of user ids by occurrence */
const { dict } = require('./101-data');
const newDict = {};
for (const [occur, userID] of Object.entries(dict)) {
  if (!newDict[userID]) {
    newDict[userID] = [];
  }
  newDict[userID].push(occur);
}
console.log(newDict);
