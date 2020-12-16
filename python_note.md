### zip 
````python
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = tuple(zip(a, b))
y = list(zip(a, b))

print(x)
print(y)

for el in x:
    print(el[0])
````