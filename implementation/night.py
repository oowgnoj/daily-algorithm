# This is coding test 117 page
[row, column]= str(input())

row = int(ord(row)- 96)
column = int(column)
cnt = 0
cases = [(2,1), (2,-1), (-2, 1), (-2, -1), (1,2), (1, -2), (-1,2), (-1,-2)]
for case in cases:
    if 1 <= row + case[0] <=8  and 1<= column + case[1] <=8:
        cnt += 1
print(cnt)