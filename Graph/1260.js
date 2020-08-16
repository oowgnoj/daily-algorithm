/*

# 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.

#출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력
1 2 4 3
1 2 3 4
*/

class Node {
  constructor(number) {
    this.number = number;
    this.adj = [];
    this.visited = false;
  }
  enqueue = (Node) => {
    if (this.adj !== []) {
      let node = this.adj.unshift(Node);
      return node;
    }
  };
  dequeue = () => {
    let node = this.adj.pop();
    return node;
  };
}

// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

console.log(
  require("fs").readFileSync("/dev/stdin").toString().trim().split("")
);

// rl.question("", (info) => {
//   const [Nnode, Nvertex, Nstart] = info.split(" ").map((el) => parseInt(el));

//   rl.close();
//   console.log("dd");
// });

// function getVertex(n) {
//   let i = 0;
//   let vertex = {};
//   rl.question("", (v) => {
//     let [node1, node2] = v.split(" ").map((el) => parseInt(el));
//     if (vertex[node1]) {
//       vertex[node1].adj.push(node2);
//       return;
//     } else {
//       let newNode = new Node(node1);
//       newNode.adj.push(node2);
//     }
//     if (vertex[node2]) {
//       vertex[node2].adj.push(node1);
//       return;
//     } else {
//       let newNode = new Node(node2);
//       newNode.adj.push(node1);
//     }
//   });
//   console.log(i, n);
//   if (i <= n) {
//     i = i + 1;
//     getVertex(i, n);
//   } else {
//     rl.close();
//   }
// }
