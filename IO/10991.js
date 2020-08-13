const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  nLine = parseInt(num) * 2 - 1;
  for (let i = 0; i < num; i++) {
    console.log(" ".repeat(num - i - 1) + "* ".repeat(i + 1));
  }
});
