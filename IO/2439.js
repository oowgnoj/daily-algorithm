const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let nLine = parseInt(num);

  for (let i = 1; i <= nLine; i++) {
    let empty = " ".repeat(num - i);
    let star = "*".repeat(i);
    console.log(empty + star);
  }
  rl.close();
});
