#!/usr/bin/node

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

function add (num1, num2) {
  if (!num1 || !num2) {
    console.log('NaN');
  }
  console.log(num1 + num2);
}

add(num1, num2);
