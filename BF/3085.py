
# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.



# 5
# YCPZY
# CYZZP
# CCPPP
# YCYZC
# CPPZZ

# 4

def check(lst):
    dic = {'Y':1, 'C':1, 'P':1, 'Z':1}
    for i in range(1,len(lst)):
        cnt = 1
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                cnt +=1
            else:
                break
        if cnt > dic[lst[i]]:
            dic[lst[i]] = cnt
    return dic[max(dic)]
        

def flat_nested_list(lst, n):
    ans = []
    for i in range(len(lst)):
        ans.append(lst[i][n])
    return ans

num = int(input())
lst = []
for i in range(num):
    lst.append(list(input()))

ans = 0


for i in range(num):
    for j in range(num):

        if j < num-1:
            # row change
            row_temp = lst.copy()
            tmp = row_temp[i][j]
            row_temp[i][j] = row_temp[i][j+1]
            row_temp[i][j+1] = tmp

            row_max = max(check(row_temp[i]), check(row_temp[i+1]), check(flat_nested_list(row_temp,j)), check(flat_nested_list(row_temp,j+1)))

            if ans < row_max:
                ans = row_max

            tmp = row_temp[i][j]
            row_temp[i][j] = row_temp[i][j+1]
            row_temp[i][j+1] = tmp
        
        if i < num-1:
            # column change
            col_temp = lst.copy()
            tmp = col_temp[i][j]
            col_temp[i][j] = col_temp[i+1][j]
            col_temp[i+1][j] = tmp
            col_max = max(check(col_temp[i]), check(col_temp[i+1]), check(flat_nested_list(row_temp,j)), check(flat_nested_list(row_temp,j+1)))
            
            if ans < col_max:
                ans = col_max
            
            tmp = col_temp[i][j]
            col_temp[i][j] = col_temp[i+1][j]
            col_temp[i+1][j] = tmp
            



print(ans)
