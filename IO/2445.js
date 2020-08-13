/*
 *        *
 **      **
 ***    ***
 ****  ****
 **********
 ****  ****
 ***    ***
 **      **
 *        *
 */

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let nLine = parseInt(num);
  for (let i = 1; i <= nLine; i++) {
    index = i;
    if (index >= 6) {
      index = index % 5;
    }
    let empty = " ".repeat(5 - index);
    let star = "*".repeat(index);
    let print = star + empty;
    let reverse = print.split("").reverse().join("");
    console.log(print + reverse);
  }
  rl.close();
});
