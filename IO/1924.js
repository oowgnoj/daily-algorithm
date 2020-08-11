// 2007년

// input은 M D 형태
// output MON... SUN
// 1 1 -> MON
// 1,3,5,7,8,10,12 : 31일
// 4,6,9,11 : 30일
// 2 : 28일
const monthMaxDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// 1차 풀이
// rl.on("line", (MD) => {
//   let [M, D] = MD.split(" ").map((el) => parseInt(el));
//   let mDays = 0;
//   for (let i = 1; i < M; i++) {
//     mDays += monthMaxDays[i];
//   }
//   let ans = mDays + D - 1;
//   let daysOffset = days[ans % 7];
//   console.log(daysOffset);
//   rl.close();
// });

// best solution
rl.on("line", (MD) => {
  let [M, D] = MD.split(" ").map((el) => parseInt(el));

  let dayOffset = new Date(`2007-${M}-${D}`).getDay();
  console.log(days[dayOffset]);
  rl.close();
});
/*
console.log(day[new Date("2018-"+input[0]+"-"+input[1]).getDay()]);
new Date 객체를 만들어, getDay() 메소드를 사용했다.
*/
