const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let nLine = parseInt(num);
  for (let i = nLine; i >= 1; i--) {
    let star = "*".repeat(i);
    console.log(star);
  }
  rl.close();
});
