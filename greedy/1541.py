lst=input().split('-') # -로 split한다움


ans = sum(map(int, lst[0].split('+')))
for i in range(1, len(lst)):
    ans -= sum(map(int, lst[i].split('+')))
print(ans)



# stop = 0
# isOpen = False
# ans = ''
# for i, el in enumerate(string):
#     if el == '-':
#         if isOpen:
#             ans += ')'+ el + '('
#             isOpen = True
#             continue
#         ans += el + '('
#         isOpen = True
#         continue

#     else:
#         if i >= 1 and string[i-1] == '+' or string[i-1] == '-':
#             if string[i] == '0':
#                 continue
#     ans += el
# if isOpen :
#     ans += ')'
# print(eval(ans))
