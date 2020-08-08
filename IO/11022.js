const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
var count = 0;

var func = function () {
  rl.question("", function (n) {
    plusTwoNum(parseInt(n));
  });
};

var plusTwoNum = function (n) {
  rl.question("", function (el) {
    [a, b] = el.split(" ").map((el) => parseInt(el));
    console.log(`Case #${count + 1}: ${a} + ${b} = ${a + b}`);
    count = count + 1;
    if (count == n) {
      rl.close();
    }
    plusTwoNum(n);
  });
};

func();
