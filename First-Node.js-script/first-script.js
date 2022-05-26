const fs = require('fs');
console.log('Script');

fs.writeFileSync('test.txt','File');
fs.appendFileSync('./test.txt','Appended value');
const text = fs.readFileSync('./test.txt',{ encoding: 'utf8' });
console.log(text);