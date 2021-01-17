n = int(input())
t = int(input())

start = 1
end = pow(2, n)

while True:
    mid = (start+end)//2
    for i in range(n):
        # if pow(2, i) <= t <= pow(2, i+1)
