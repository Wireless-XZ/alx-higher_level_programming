#!/usr/bin/node
const args = process.argv;

if (args[2] && Number.parseInt(args[2])) {
  console.log('My number: ' + Number.parseInt(args[2]));
} else {
  console.log('Not a number');
}
