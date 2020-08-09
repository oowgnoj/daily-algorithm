const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let dan = parseInt(num);
  let i = 1;
  while (i <= 9) {
    console.log(`${dan} * ${i} = ${dan * i}`);
    i++;
  }
});
