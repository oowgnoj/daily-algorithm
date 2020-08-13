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
  let nLine = parseInt(num);
  for (let i = 0; i <= nLine; i++) {
    let fullStarts = "*********";
    // console.log(left);
  }
  rl.close();
});
