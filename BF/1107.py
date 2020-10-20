<<<<<<< HEAD
# 5457
# 3
# 6 7 8

# 6


# 500000
# 8
# 0 2 3 4 6 7 8 9

# 11117

# 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  
# 둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 
# 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.



NOW = 100
target = int(input())
num_of_broken = int(input())

if num_of_broken !=0:
    broken_nums = list(map(int, str(input()).split(' ')))
    origin = [0,1,2,3,4,5,6,7,8,9]
    avail_nums = list(set(origin) - set(broken_nums))
else:
    avail_nums = [0,1,2,3,4,5,6,7,8,9]

def getCount (target):
    count = 0
    lst = list(str(target))
    for i in range(len(lst)):
        digit = pow(10,len(lst)-i-1)
        num = int(lst[i])
        if num in avail_nums:
            count+=1
        else:
            similar = 100
            for el in avail_nums:
                if abs(num - el) < abs(num - similar):
                    similar = el
            count += 1
            count += digit * abs(num - similar)
    return count

a = abs(target - NOW)
count = getCount(target)
alter = count


for i in range(1, count):
    times = min(getCount(target+i), getCount(target-i)) + i
    if alter > times:
        alter = times
ans = min(count, a,alter)
print(ans)



# 9999 -> 8888 에서 가는게 아니라 10000 에서 - 1 하면 된다. 이것을 처리를 안했다.

# 고장난 버튼을 누르면 Fasle
=======
# https://www.acmicpc.net/problem/1107
>>>>>>> 492b721751076ca702472eaaf1315e20f1ac5fa8
