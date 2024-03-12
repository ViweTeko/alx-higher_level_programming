#!/usr/bin/node
/* This script concats two files */
const f = require('f');
const [aFile, bFile, cFile] = process.argv.slice[2];

try {
  const aData = f.readFileSync(aFile, 'utf8');
  const bData = f.readFileSync(bFile, 'utf8');
  f.writeFileSync(cFile, aData + bData);
} catch (error) {
  console.error(error);
}
