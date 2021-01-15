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


### lambda
````
meets.sort(key=lambda x: (x[1], x[0]))

````

### map(func, list)
인자로 함수와, 리스트를 받는다. 리스트의 각 요소에 function을 적용하고, map object를 return 한다.
아래 예시를 보면 map object의 주소를 return 하는데, 이 때 map 객체는 이터레이터 라고 한다. 따라서 list 혹은 tuple로 감싸주면 원하는 값을 얻을 수 있다.
````python
print(map(lambda x: x *2, [1,2,3])
# <map object at 0x1025269d0>
````

#### 이터레이터
`iter`는 반복 가능한 데이터 타입을 인자로 받는다. (예, list, tuple)
````python
print(iter([1,2,3]))
<list_iterator object at 0x10216bee0>

a= iter([1,2,3])
print(a)
print(next(a))
print(next(a))
print(next(a))

# <list_iterator object at 0x10216bee0>
# 1
# 2
# 3

````

