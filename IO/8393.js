const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let total = 0;
  for (let i = 1; i <= parseInt(num); i++) {
    total += i;
  }
  console.log(total);
  rl.close();
});
