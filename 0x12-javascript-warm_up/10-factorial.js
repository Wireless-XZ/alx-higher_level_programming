#!/usr/bin/node
function fac (x) {
  if (x > 1) {
    return (x * fac(x - 1));
  } else {
    return (1);
  }
}

console.log(fac(Number.parseInt(process.argv[2])));
