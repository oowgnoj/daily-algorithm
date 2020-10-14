# 첫째 줄에 E S M으로 표시되는 가장 빠른 연도를 출력한다. 1 1 1은 항상 1이기 때문에, 정답이 음수가 나오는 경우는 없다.

# E = 15
# S = 28
# M = 19
# ex
# 15 28 19
# 7980

# 1 2 3
# 5266


# x를 찾아야 되는데, 
# x = (15 * i + E) == (28 * j + S)  == (19* k + M)

[E, S, M]= list(map(int, str(input()).split(' ')))

i = 1
a = 0
b = 0
c = 0

ans = 1
while True:
    first = 15 * a + E
    second = 28 * b + S
    third = 19 * c + M

    if i % 15 ==0:
        a +=1
    if i % 28 ==0:
        b +=1
    if i % 19 == 0:
        c +=1
    if first == second == third:
        ans = first
        break
    else:
        i += 1

print(ans)