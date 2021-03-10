# Lv2 가장 큰 정사각형 찾기
def solution(board):
    row, col = len(board), len(board[0])
    case = []
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] != 0:
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) + 1
                case.append(board[i][j])
    if case:
        return pow(max(case), 2)
    else:
        return pow(max(sum(board, [])), 2)