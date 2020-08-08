const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

var plusTwoNum = () => {
  rl.question("", function (el) {
    [a, b] = el.split(",").map((el) => parseInt(el));
    if (a === 0 && b === 0) {
      rl.close();
    }
    console.log(a + b);
    plusTwoNum();
  });
};

plusTwoNum();
