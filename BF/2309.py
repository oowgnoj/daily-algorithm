# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 
# 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 9명의 난쟁이 중에서 7명의 난쟁이를 추려낸다.
# 7명의 난쟁의 키의 합은 100이다.


num = 9
lst = []
no = []
for i in range(num):
    lst.append(int(input()))

total = sum(lst)
for i in range(num-1):
    for j in range(i+1, num):
        output = total - lst[i] - lst[j]
        if output == 100:
            no.append(lst[i])
            no.append(lst[j])
            break
    else:
        continue
    break

lst.sort()
for el in lst:
    if el not in no:
        print(el)


    