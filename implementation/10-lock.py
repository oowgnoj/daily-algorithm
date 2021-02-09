# 열쇠를 끼워보는 함수
# 현재 board offset x, y
def solve(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[i+x][j+y] += key[i][j]

# 끼웠던 열쇠 돌려놓기
def revert(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[i+x][j+y] -= key[i][j]

def rotate_90(matrix):
    return list(zip(*matrix[::-1]))


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True




def solution(key, lock):
    M, N = len(key), len(lock)
    board = [[0]*(M*2 + N) for _ in range(M*2 + N)]
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    for _ in range(4):
        for x in range(M+N):
            for y in range(M+N):
                rotated_key = rotate_90(rotated_key)
                solve(x, y, M, rotated_key, board)
                if check(board, M, N):
                    return True
                revert(x, y, M, rotated_key, board)
                
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]]	, [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))