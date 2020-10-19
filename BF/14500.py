
# shape_one = [[[i, j], [i+1, j], [i+2, j], [i+3, j]
#              ]], [[i, j], [i, j+1], [i, j+2], [i, j+3]]

# shape_two = [[i, j], [i+1, j], [i, j+1], [i+1, j+1]]

# shape_three = [[[i, j], [i, j+1], [i, j+2], [i+1, j+2]], [[i, j], [i+1, j], [i+2, j], [i, j+1], [[i, j], [i+1, j], [i+1, j+1], [i+1, j+2]], [[i, j], [i, j+1], [i+1, j], [i+2, j]]

# four = [[[i, j], [i, j+1], [i+1, j+1], [i+1, j+2]],
#     [[i+1, j], [i, j+1], [i, j+2], [i+3, j]]

# five = [(0, 0), (1, 0), (1, 1), (2, 0)], [(0, 1), (1, 0), (1, 1), (2, 1)], [(0, 0)(0, 1)(0, 2)(1, 1)][(0, 1)(1, 0), (1, 1), (1, 2)]

shapes = [[[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [0, 1], [0, 2], [0, 3]], [[0, 0], [1, 0], [0, 1], [1, 1]], [[0, 0], [0, 1], [0, 2], [1, 2]], [[0, 0], [1, 0], [2, 0], [0, 1]], [[0, 0], [1, 0], [1, 1], [1, 2]], [[0, 0], [0, 1], [1, 0], [2, 0]], [[0, 0], [0, 1], [1, 1], [1, 2]], [[1, 0], [0, 1], [0, 2], [3, 0]], [[1, 0], [1, 0], [1, 1], [2, 0]], [[0, 1], [1, 0], [1, 1], [2, 1]], [[0, 0], [0, 1], [0, 2], [1, 1]], [[0, 1], [1, 0], [1, 2], [1, 1]]
          ]
[N, M] = list(map(int, str(input()).split(' ')))
lst = []
ans = 0


def listSum(list1, list2):
    return [list1[0] + list2[0], list1[1] + list2[1]]


for i in range(N):
    lst.append(list(map(int, str(input()).split(' '))))


def getIndex(index):
    [i, j] = index
    try:
        return lst[i][j]
    except:
        return 0


for i in range(N):
    for j in range(M):
        for i in range(len(shapes)):
            temp = getIndex(listSum([i, j], shapes[i][0])) + getIndex(listSum([i, j], shapes[i][1])) + getIndex(listSum(
                [i, j], shapes[i][2])) + getIndex(listSum([i, j], shapes[i][3]))
            if temp > ans:
                ans = temp

print(ans)
