#!/usr/bin/node

const size = Number(process.argv[2]);
const x = 'X';

if (!size || isNaN(size)) {
  console.log('Missing size');
}

for (let i = 0; i < size; i++) {
  console.log(x.repeat(size));
}
