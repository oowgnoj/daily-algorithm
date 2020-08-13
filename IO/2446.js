// *********
//  *******
//   *****
//    ***
//     *
//    ***
//   *****
//  *******
// *********

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let nLine = parseInt(num) * 2 - 1;
  for (let i = 0; i < num; i++) {
    console.log(" ".repeat(i) + "*".repeat(nLine - 2 * i));
  }
  for (let i = 2; i <= num; i++) {
    empty = nLine - (i * 2 - 1);
    console.log(" ".repeat(empty / 2) + "*".repeat(i * 2 - 1));
  }
  rl.close();
});
