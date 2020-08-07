const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

var plusTwoNum = () => {
  rl.question("", function (el) {
    [a, b] = el.split(" ").map((el) => parseInt(el));
    console.log(a + b);
    plusTwoNum();
  });
};

plusTwoNum();
