#!/usr/bin/node

const n = Number(process.argv[2]);

function factorial (n) {
  if (isNaN(n) || n <= 0) {
    return 'Not a number';
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
