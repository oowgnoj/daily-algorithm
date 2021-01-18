a, b = map(int, input().split(" "))  # 인풋으로 주어진 값을 공백을 기준으로 나눈다.
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
