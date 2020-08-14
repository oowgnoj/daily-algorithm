const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  if (parseInt(num) === 1) {
    console.log("*");
    return;
  } else {
    for (let i = 1; i < parseInt(num); i++) {
      let front = " ".repeat(num - i) + "*";
      let back = i >= 2 ? " ".repeat((i - 1) * 2 - 1) + "*" : "";
      console.log(front + back);
    }
    console.log("*".repeat(num * 2 - 1));
  }
});
