

def convert_to_str (a,b,c):
    return '/'.join(map(str, [a,b,c]))

memo = {}

for i in range(0, 21):
    for j in range(0, 21):
        for k in range(0, 21):
            if i <= 0 or j <= 0 or k<= 0:
                memo[convert_to_str(i,j,k)] = 1
            elif i < j and j < k:
                memo[convert_to_str(i,j,k)]= memo[convert_to_str(i,j,k-1)] + memo[convert_to_str(i,j-1,k-1)] - memo[convert_to_str(i,j-1,k)]
            else:
                memo[convert_to_str(i,j,k)]= memo[convert_to_str(i-1,j,k)] + memo[convert_to_str(i-1,j-1,k)]+ memo[convert_to_str(i-1,j,k-1)] - memo[convert_to_str(i-1,j-1,k-1)]




while True:
    case = list(map(int, input().split(' ')))
    if case == [-1, -1, -1]:
        break
    else:
        a,b,c = case
        if min(a,b,c) <= 0:
            print(f'w({a}, {b}, {c}) = 1')
            continue
        elif max(a,b,c) > 20:
            print(f'w({a}, {b}, {c}) = {memo[convert_to_str(20,20,20)]}')
        else:
            print(f'w({a}, {b}, {c}) = {memo[convert_to_str(a,b,c)]}')

