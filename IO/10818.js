const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

arr = [];

rl.question("", () => {
  rl.question("", (numbers) => {
    arr = numbers.split(" ").map((el) => parseInt(el));

    console.log(`${Math.min(...arr)} ${Math.max(...arr)}`);
    rl.close();
  });
});

/*
런타임에러 발생 상황

배열에 할당된 크기를 넘어서 접근했을 때
전역 배열의 크기가 메모리 제한을 초과할 때
지역 배열의 크기가 스택 크기 제한을 넘어갈 때
0으로 나눌 떄
라이브러리에서 예외를 발생시켰을 때
재귀 호출이 너무 깊어질 때
이미 해제된 메모리를 또 참조할 때
프로그램(main 함수)이 0이 아닌 수를 반환했을 때

https://www.acmicpc.net/board/view/50381


*/
