nums = list(map(int,str(input()).split(' ')))

GDC = 0
for i in reversed(range(min(nums[0],nums[1])+1)):
    if nums[0] % i == 0 and nums[1] % i ==0:
        GDC = i
        break

LCM = GDC * nums[0] / GDC * nums[1] / GDC
print(GDC)
print(int(LCM))