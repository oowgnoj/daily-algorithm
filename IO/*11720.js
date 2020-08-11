const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (answer) => {
  const str = String(answer);
  let ans = "";
  for (let i = 0; i < str.length; i++) {
    ans += str[i];
    if (ans.length === 10) {
      console.log(ans);
      ans = "";
    } else if (i === str.length - 1) {
      console.log(ans);
    }
  }
  rl.close();
});

/*
sapphire 님의 코드.
map으로 10번째가 될 때 \n 을 붙여줘서 띄어쓰기를 하고 출력했다. 
 */

console.log(
  require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("")
    .map(function (e, i) {
      return (i % 10 === 0 ? "\n" : "") + e;
    })
    .join("")
    .trim()
);
