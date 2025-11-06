#!/usr/bin/node

const sentence = 'C is fun';
const x = process.argv[2];

function printXtimes (arg) {
  for (let i = 0; i < arg; i++) {
    console.log(sentence);
  }
}

printXtimes(x);
