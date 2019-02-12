#!/usr/bin/node
// a scrip that prints a message depending of the number of args.
// use console.log() to print output.

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}