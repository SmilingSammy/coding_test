# 다음 큰 숫자
from collections import Counter

def solution(n):
    n_bin = bin(n)[2:]
    one_cnt = Counter(list(n_bin))['1']

    for i in range(n+1, 1000001):
        i_bin = bin(i)[2:]
        tmp_one_cnt = Counter(list(i_bin))['1']

        if one_cnt == tmp_one_cnt:
            break

    return i

