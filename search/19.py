# 14888
from collections import deque
import copy
import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int,input().split(' ')))
plus,minus,multiply,divide = map(int,input().split(' ')) # + - * /

max_values = []
min_values = []
index = 0
# 숫자배열의 요소가 다 끝날 때 까지
queue = deque([[numbers[0], plus,minus,multiply,divide]])
numbers = deque(numbers[1:])

sign_map = ['+', '-', 'x', '/']

while True:
    if not numbers:
        lst = [i[0] for i in queue]
        print(max(lst))
        print(min(lst))
        break
    next_value = numbers.popleft()
    temp = deque()
    while queue:

        case = queue.popleft()
        for i in range(4):
            cur_value,plus,minus,multiply,divide = case
            if i == 0 and plus:
                plus -= 1
                calculated = cur_value + next_value
                temp.append([calculated,plus,minus,multiply,divide])
            if i == 1 and minus:
                minus -= 1
                calculated = cur_value - next_value 
                temp.append([calculated,plus,minus,multiply,divide])
            if i == 2 and multiply:
                multiply -= 1
                calculated = cur_value * next_value
                temp.append([calculated,plus,minus,multiply,divide])
            if i == 3 and divide:
                if next_value == 0:
                    continue
                divide -= 1
                calculated = abs(cur_value) // next_value
                if cur_value < 0:
                    calculated = -1*calculated
                temp.append([calculated,plus,minus,multiply,divide])
    queue=temp








