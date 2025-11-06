#!/usr/bin/node

const sentence = 'C is fun'
const x = process.argv[2];

function print_x_times(arg) {
  for (let i = 0; i < arg; i++) {
    console.log(sentence);
  }
}

print_x_times(x)
