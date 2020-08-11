const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (num) => {
  let i = 1;
  to = parseInt(num);
  while (i <= to) {
    console.log(i);
    i++;
  }
  rl.close();
});
