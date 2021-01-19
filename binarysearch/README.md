### 이분 탐색
배열이 정렬되어 있을 때 사용할 수 있는 탐색 알고리즘이다. 시간 복잡도는 최대 O(logN)이다.

#### 순차 탐색
`array = [1,2,3,4,5]` 에서 k=5 을 찾는다고 해보자.

순차 탐색으로 array 내부에서 5값을 찾는다고 하면 아래와 같이 O(N) 시간복잡도로 찾을 수 있다.

````python
for el in array:
	if el == k:
			print('True')
````

#### 이분 탐색

이분 탐색을 사용해 k=5 를 찾는 코드는 아래와 같다.

````python
def binary_search(array, k, start, end):
  if start > end: # 탈출 코드
    return None
  
  mid = (start+end)//2
  if array[mid] == k:
    return mid 
  elif array[mid] > k:
    return binary_search(array, k, start, mid-1)
  else:
    return binary_search(array, k, mid+1, end)
  
binary_search([1,2,3,4,5], 5, 0, 4)
````

 이분 탐색은 특정 조건이 충족되면 실행을 중지하면 된다. 따라서 `while` 문이나, 재귀 함수를 사용하여 구현하기 쉬운데, 여기서 특정 조건이란 일반적인 이분 탐색의 경우 k 값을 찾았거나, logN 번까지의 탐색이 끝난 경우를 말한다.



### 이분탐색과 실생활

이분 탐색은 순차적으로 정렬되어 있는 목록(배열) 에서 사람이 찾는 방식과 가장 유사하다고 볼 수 있다. 

예시) 서점에서 알맞는 책장 찾기 (A~K)
서점이나 도서관에 가면 벽마다 A, B, C 등으로 각 분야를 나타내는 대표 문자가 있다. 아래 그림에서 찾는 책이 B(문학) 칸에 있다고 해보자. 
책장에 글씨가 잘 보이지 않아 대충 가운데 쯤으로 가보니 E칸에 있었다. 왼쪽 저 멀리에 A가 보였고 오른쪽에는 H,I 책장이 있었다.
1. 배열로 그대로 옮겨보면 [A,B,C,D,E,F,G,H,I] 에서 현재 4번째 index에 해당하는 E칸에 있다.
2. 목적지는 B 칸 이므로 뒤로하고 A칸 쪽을 향해 간다.
3. 한 반쯤 와서 벽장을 쳐다보니 B(문학)칸 앞에 있었다. 
4. 찾았다.

만약 순차탐색의 방식으로 시작(A)부터 하나씩 모든 벽면을 통과하며 찾으면 **평균적으로는 O(N/2), 최악의 경우 O(N) 시간이 걸린다.** 반면 이분탐색을 사용하면 **최대 O(logN) 번이 소요된다.** 따라서 이분탐색은 비교적 큰 규모의 탐새에서 더욱 더 성능을 발휘한다. 하지만 **정렬이 되어있지 않은 경우엔 이분탐색을 사용할 수 없다. (책장이 A,D,F,E 등 무작위 순으로 배치가 되어있는 경우를 생각해보면 된다.)**




### 이분 탐색의 대표유형

주로 문제에서 10억 이상의 N 값과 1초의 시간이 주어진다거나, 정렬 되어있는 배열을 탐색 혹은 감이 잘 오지않는 최적화 문제(최대/최소 값)가 주어진 경우 이분 탐색을 활용할 수 있다.

1. 큰 범위 내에서 탐색하기

   대표적인(가장 쉬운) 이분탐색 유형으로 큰 N 범위 (1 <= N <= 1,000,000,000) 에서 특정 요소의 유/무, index 등을 리턴하는 함수를 구현하는 것이다. 아래 이분 탐색 코드 유형을 사용하면 풀리는 문제들이다. (백준 1920, 10816 포함)

   ````python
   def binary_search(array, k, start, end):
     if start > end: # 탈출 코드
       return None
     
     mid = (start+end)//2
     if array[mid] == k:
       return mid 
     elif array[mid] > k:
       return binary_search(array, k, start, mid-1)
     else:
       return binary_search(array, k, mid+1, end)
     
   binary_search([1,2,3,4,5], 5, 0, 4)
   ````

   ***특정 요소의 유/무만을 판단하는 경우라면 집합 자료형을 고려해 볼 필요가 있다.***

2. 특정 수의 갯수 구하기

   다음은 배열 내부에서 특정 수의 갯수를 구하는 문제인데, 정렬되어 있는 리스트에서 **중복된 요소의 시작, 끝 index를 찾는 방법으로 해결이 가능하다.** 아래 코드는 이분 탐색을 통해 직접 시작, 끝 인덱스를 찾는 함수를 구현했지만, 파이썬의 `bisect` 라이브러리를 사용하면 더욱 쉽게 해결할 수 있다.

   [백준 10816 숫자 카드](https://www.acmicpc.net/problem/10816)

   ````python
   import sys
   input = sys.stdin.readline
   n = int(input())
   lst = list(map(int, input().split(' ')))
   target_n = int(input())
   targets = list(map(int, input().split(' ')))
   
   lst.sort()
   
   
   def get_target_start_index(array, target, start, end):
       if start > end:
           return None
       mid = (start+end)//2
       if (mid == 0 or array[mid-1] < array[mid]) and array[mid] == target:
           return mid
       if array[mid] >= target:
           return get_target_start_index(array, target, start, mid-1)
       else:
           return get_target_start_index(array, target, mid+1, end)
   
   
   def get_target_last_index(array, target, start, end):
       if start > end:
           return None
       mid = (start+end)//2
       if (mid == end or array[mid+1] > array[mid]) and array[mid] == target:
           return mid
       if array[mid] <= target:
           return get_target_last_index(array, target, mid+1, end)
       else:
           return get_target_last_index(array, target, start, mid-1)
   
   
   for el in targets:
       start = get_target_start_index(lst, el, 0, len(lst)-1)
       end = get_target_last_index(lst, el, 0, len(lst)-1)
       if start == None or end == None:
           print(0)
       else:
           print(end-start+1)
   
   ````

   

3. 파라메트릭 검색 (parametric search)

   **최적화 문제를 결정(YES/NO) 문제로 바꾸어 이분탐색을 통해 여러번 시도하며 최적해를 찾는다.** 파라메트릭 문제는 첫 눈에 이분 탐색 문제로 잘 보이지 않지만 마찬가지로 큰 범위와 짧은 시간제한이 있고 문제에서 "최대, 최소 등의 단어가 나올 수 있다."

   

   

### 이분 탐색 풀이시 주의사항

이분 탐색을 PS에 활용하는 경우 **시간과 입력의 최대값을 확인하여 O(logN) **으로 풀어야 하는 경우에 적용한다. 순차 탐색이나 집합 자료형 등 더 간단하게 구현이 가능할 수 있기 때문이다. 
1. 탐색할 주체와 시작(start) 과 끝 (end) 범위를 명확히 한다.

   일반적으로 리스트 내부에서 특정 값을 찾는 경우엔 0번째 index에서 len(list) 사이에 값이 있어 명확하게 구할 수 있다. **반면에 명확하게 이분 탐색을 활용할 것 처럼 보이지 않는 문제들이나 파라메트릭(parametric) 검색 유형같은 경우 이 과정이 중요하다.**

2. 재귀함수나 while 문을 활용한다. 파라메트릭 서치는 `while` 문을 사용하는 것이 더 편하다.

3. 파라메트릭 서치 유형의 경우엔 최대값, 최소값을 구하는 유형으로 나눌 수 있다. 두개의 부등호 중 하나에 등호를 섞어야 한다는 점이다. 최솟값, 최댓값을 구하기 때문이다.