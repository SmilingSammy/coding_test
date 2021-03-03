# [1차] 프렌즈4블록

from copy import deepcopy

def remov(m, n, ls):
    b = deepcopy(ls)
    for i in range(m - 1):
        for j in range(n - 1):
            if b[i][j] == b[i + 1][j] == b[i][j + 1] == b[i + 1][j + 1] != "":
                ls[i][j] = ls[i + 1][j] = ls[i][j + 1] = ls[i + 1][j + 1] = ""
    return b, ls

def reset(m, n, ls):
    # reset_play
    for i in range(m - 1):
        for j in range(n):
            if ls[i + 1][j] == "":
                ls[i + 1][j], ls[i][j] = ls[i][j], ""
    return ls


def multi_reset(m, n, ls):
    bf_ls = None
    ls = reset(m, n, ls)

    while bf_ls != ls:
        bf_ls = deepcopy(ls)
        ls = reset(m, n, ls)

    return ls


def solution(m, n, board):
    play = [list(x) for x in board]
    b, rmv_play = remov(m, n, play)
    play = multi_reset(m, n, rmv_play)

    while b != play:
        b, rmv_play = remov(m, n, play)
        play = multi_reset(m, n, rmv_play)

    return sum(play, []).count("")