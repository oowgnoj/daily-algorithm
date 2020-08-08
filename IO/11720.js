const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (answer) => {
  rl.question("", (nums) => {
    const numArr = nums.split("").map((el) => parseInt(el));
    const sum = numArr.reduce((a, b) => a + b, 0);
    console.log(sum);
    rl.close();
  });
});
