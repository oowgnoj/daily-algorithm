# a = list(map(lambda x: x *2, [1,2,3]))
# print(a)

a= iter([1,2,3])
print(a)
print(next(a))
print(next(a))
print(next(a))

print(list.__iter__)