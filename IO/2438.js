const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let nLine = parseInt(num);
  for (let i = 1; i <= nLine; i++) {
    console.log("*".repeat(i));
  }
  rl.close();
});
