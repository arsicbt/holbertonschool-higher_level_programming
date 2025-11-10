#!/usr/bin/node

const list = process.argv.slice(2).map(Number);

if (list.length < 2) {
  console.log(0);
} else {
  let max = list[0];
  let secondMax = -Infinity;

  for (let i = 0; i < list.length; i++) {
    if (list[i] > max) {
      secondMax = max;
      max = list[i];
    } else if (list[i] > secondMax && list[i] < max) {
      secondMax = list[i];
    }
  }

  console.log(secondMax === -Infinity ? 0 : secondMax);
}
