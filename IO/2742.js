const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (num) => {
  let i = parseInt(num);
  let str = "";
  while (i > 0) {
    console.log(i);
    i--;
  }
  console.log(str);
  rl.close();
});

// 왜 안되는지 모르겠다
