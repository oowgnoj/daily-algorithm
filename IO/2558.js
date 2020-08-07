const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", function (a) {
  rl.question("", function (b) {
    a = parseInt(a);
    b = parseInt(b);
    console.log(a + b - 2);
    rl.close();
  });
});

/**
/dev/stdin

# 표준입력장치이며, 콘솔키보드 드라이버에서 값을 읽어와 입력을 받아 처리 할 수 있게 해준다.

/dev/stdout

# 표준출력장치이며, 콘솔모니터 드라이버를 구동시켜 모니터에 바로 출력할 수 있게 해준다.

/dev/stderr

표준에러장치이며, 콘솔모니터 드라이버를 구동시켜 모니터에 바로 출력할 수 있게 해준다.

cat -> 파일 읽는 리눅스 명령어

*/
