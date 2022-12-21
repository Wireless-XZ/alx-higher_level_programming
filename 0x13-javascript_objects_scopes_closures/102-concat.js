#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], (err, data) => {
  if (err) throw err;
  else {
    fs.writeFile(args[4], data, (err) => {
      if (err) throw err;
    }
    );
  }
});

fs.readFile(args[3], (err, data) => {
  if (err) throw err;
  else {
    fs.appendFile(args[4], data, (err) => {
      if (err) throw err;
    }
    );
  }
});
