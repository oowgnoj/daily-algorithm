### GREEDY

| Platform |    Title/#    |O/X| Date  |
|----------|:-------------:      |--:|------:|
| BOJ      |  DFS와 BFS/1260     | O | 202106 |
| BOJ      |  바이러스/2606      | O | 202106 |
| BOJ      |  단지번호붙이기/11045        | O | 202106 |
| BOJ      |  ATM 0/11399       | O | 202106 |
| BOJ      |  ATM 0/13305       | O | 202107 |


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