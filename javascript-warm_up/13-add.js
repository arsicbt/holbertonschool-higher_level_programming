#!/usr/bin/node

function add (n1, n2) {
  if (isNaN(n1) || isNaN(n2)) {
    return 'Add at least two numbers ;)'
  }
  return n1 + n2;
}

module.exports.add = add;
