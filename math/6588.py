import sys

arr = [_ for _ in range(1000001)]
check = [True for _ in range(1000001)]
check[0] = False
check[1] = False
num = 1000000
for i in range(2, int(num ** 0.5)+1):
    if check[i] == True:
        for j in range(i+i, num, i):
            check[j] = False

input = sys.stdin.readline


while True:
    input_num = int(input())
    if input_num == 0:
        break
    for i in range(3, num):
        if check[i] == True:
            if check[input_num-i] == True:
                print("%d = %d + %d" % (input_num, i, input_num-i))
                break
