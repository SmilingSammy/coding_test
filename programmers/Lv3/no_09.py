# Lv3 경주로 건설

from collections import deque
import math


def solution(board):
    # 좌 하 상 우
    dx = [0, 1, -1, 0]
    dy = [-1, 0, 0, 1]

    N = len(board)
    arr = [[[math.inf] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque()

    queue.append([0, 0, -1])
    arr[0][0] = [0, 0, 0, 0]

    while queue:
        x, y, direction = queue.popleft()
        for i in range(4):
            # 후진은 의미없음
            if i + direction == 3:
                continue

            nx = x + dx[i]
            ny = y + dy[i]

            cost = 100

            # 코너링
            if i != direction and direction != -1:
                cost += 500

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and arr[nx][ny][i] > cost + arr[x][y][direction]:
                arr[nx][ny][i] = cost + arr[x][y][direction]
                queue.append([nx, ny, i])

    return min(arr[N - 1][N - 1])
