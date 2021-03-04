# 순위 검색
from itertools import product
from collections import deque
def solution(info, query):
    info_dict = {}
    for elem in info:
        elem = elem.split(" ")
        elem_ls = [[elem[i], '-'] for i in range(4)]
        combination = list(product(*elem_ls))
        combination = list(map(lambda x: ''.join(x), combination))
        for key in combination:
            if key in info_dict:
                info_dict[key].append(elem[-1])
            else:
                info_dict[key] = deque([elem[-1]])
    result = []
    for q in query:
        key, score = q.replace(" and ", "").split(" ")
        if score == "-":
            count = len(info_dict[key])
        else:
            if key in info_dict:
                count = len(list(filter(lambda x: int(x) >= int(score), info_dict[key])))
            else:
                count = 0
        result.append(count)
    return result