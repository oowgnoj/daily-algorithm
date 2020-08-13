// 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

/*
 *
 **
 ***
 **
 *
 */

// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// let stack = [];

// rl.on("line", (num) => {
//   let nLine = parseInt(num) * 2 - 1;
//   let isPushing = true;
//   for (let i = 1; i <= nLine; i++) {
//     if (!isPushing) {
//       stack.pop();
//       if (stack.length === 0) {
//         isPushing = !isPushing;
//       }
//     }
//     if (isPushing) {
//       stack.push("*");
//     }
//     if (stack.length === 3) {
//       isPushing = !isPushing;
//     }
//     let stars = stack.join("");
//     a = " ".repeat(3 - stars.length) + stars;
//     console.log(a);
//   }
//   rl.close();
// });

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let numLine = num * 2 - 1;
  let answer = "";
  for (let i = 1; i <= numLine; i++) {
    if (i <= num) {
      answer += "*";
    } else {
      answer = answer.substring(0, answer.length - 1);
    }
    let foward = answer + " ".repeat(num - answer.length);
    let backward = foward.split("").reverse().join("");
    console.log(foward + backward);
  }
  rl.close();
});
