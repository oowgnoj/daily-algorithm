### BFS / DFS
## 인접 행렬 vs 인접 리스트
(a, b) 순서 쌍으로 간선이 주어질 때


### 인접 행렬
````python
adj_matrix = [[0 for i in range(N+1)] for i in range(N+1)]
adj_matrix = [[]] + adj_matrix


for i in range(M):
    [a, b]= list(map(int, input().split(' ')))
    adj_matrix[a][b] = 1
    adj_matrix[b][a] = 1
````

### 인접 리스트
````python
for i in range(edges_n):
    [a, b]=list(map(int, input().split(' ')))
    edges[a].append(b)
    edges[b].append(a)

````

인접행렬의 경우 공간적으로 많이 차지하지만 O(1)로 간선의 여부를 확인할 수 있음. 반면 인접 리스트는 간선의 여부를 최대 O(N)으로 확인 가능하다.
구현적으로는 인접 리스트가 조금 더 쉽고 깔끔하게 나오는 것 같다.



### 탐색(BFS/DFS) 문제 유형
1. BFS/DFS 개념 및 간단한 구현
- 문제에서 요구하는 최적해를 찾기 위해 BFS 혹은 DFS를 사용한다.
- 일반적으로 BFS/DFS 중 아무거나 사용하거나, 두개 모두의 결과를 요구하기도 한다.

2. matrix 형태가 주어지고, ***인접한 행렬간에 이동이 가능한 경우 matrix의 그룹으로 나눈다거나 그룹의 개수를 세는 경우다.*** 
- matrix(i, j)의 이중 루프로 **BFS/DFS 탐색을 사용해 해결한다.**
- `visited` 배열의 방문 표시를 바탕으로 탐색을 할지/안할지를 결정한다. 문제마다 요구하는 값들이 다른 경우가 많아 문제를 잘 읽어보는 것이 좋다.

3. 최단거리(BFS)
- BFS를 사용하면 A->B의 최단거리를 구할 수 있다.
- 거리(시간)을 측정하기 위해 한 노드에서 연결 되어있는 노드를 모두 추가하고, count를 올려주는 방식으로 진행한다.
    - `queue` 내부에서 temp queue를 사용하거나, for element in queue를 사용할 수 있다.
- 최단거리를 구하는 경우 위의 문제와 결합되어 matrix에서 상, 하, 좌, 우에 인접해 있는 문제들이 자주 출제되는 것 같다.

4. (심화) 최단거리
- 최단거리를 구할 때 **상태** 가 포함되는 경우. (e.g. 최대 1번 벽을 부실 수 있다 등)
- 앞선 문제들에서는 좌표(x,y) / 노드의 번호가 queue의 인자로 사용된다.
- 각 상태에 따라 독립적인 경우로 만들어주기 위해 **queue의 요소에 상태를 추가하고, visited 배열에도 필요하다면 상태를 추적할 수 있게 추가해준다.**
