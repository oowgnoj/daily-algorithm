num = str(input())

mid = len(num)//2
front = sum(list(map(int, num[:mid]))) 
back = sum(list(map(int, num[mid:]))) 

print("LUCKY" if front == back else "READY")