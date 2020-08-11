const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let nLine = parseInt(num);
  for (let i = 1; i <= nLine; i++) {
    let totalSpaceNum = nLine * 2 - 1;
    let numOfStars = 2 * i - 1;
    let stars = "*".repeat(numOfStars);
    let space = " ".repeat((totalSpaceNum - numOfStars) / 2);
    console.log(space + stars + space);
  }
  rl.close();
});
