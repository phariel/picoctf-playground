const fs = require("fs");

let temp = fs.readFileSync('./temp.txt', 'utf-8');

temp = temp.split(" \n");
temp = temp.map((v) => {
    return String.fromCharCode(v);
});

console.log(temp.join(''));