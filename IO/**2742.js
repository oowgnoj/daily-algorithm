const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (input) => {
  let num = parseInt(input);
  for (let i = num; i >= 1; i--) {
    console.log(i);
  }
  rl.close();
});

// 왜 안되는지 모르겠다

// rl.question("", (num) => {
//   let i = parseInt(num);
//   while (i >= 1) {
//     console.log(i);
//     i--;
//   }
//   rl.close();
// });
