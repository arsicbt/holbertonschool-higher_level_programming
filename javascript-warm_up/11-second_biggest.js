#!/usr/bin/node

const list = process.argv.slice(2).map(Number);

if (list.length < 2) {
  console.log(0);
} else {
  let max = list[0];
  for (let i = 0; i < list.length; i++) {
    if (list[i] > max) {
      max = list[i];
    }
  }
  console.log(max);
}
