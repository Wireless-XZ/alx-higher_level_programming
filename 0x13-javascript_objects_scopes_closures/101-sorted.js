#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  if (dict[key].toString() in newDict) {
    newDict[dict[key].toString()].push(key.toString());
  } else {
    newDict[dict[key].toString()] = [key.toString()];
  }
}

console.log(newDict);
