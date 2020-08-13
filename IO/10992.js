const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  nLine = parseInt(num) * 2 - 1;
  for (let i = 1; i <= num; i++) {
    if (i == 1) {
      console.log(" ".repeat(num - i + 1) + "*");
    } else if (i == num) {
      console.log("*".repeat(nLine));
    } else {
      console.log(" ".repeat(num - i) + "*" + " ".repeat(i * 2 - 1) + "*");
    }
  }
});
