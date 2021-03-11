# Lv2 후보키
from itertools import combinations
def solution(relation):
    row, col = len(relation), len(relation[0])
    case = []
    for i in range(1, col+1):
        case.extend(combinations(range(col), i))
    possible = []
    for c in case:
        check = [tuple(elem[key] for key in c) for elem in relation]
        if len(set(check)) == row:
            possible.append(c)
    result = set(possible[:])
    for i in range(len(possible)):
        for j in range(i+1, len(possible)):
            if len(set(possible[i])) == len(set(possible[i]) & set(possible[j])):
                result.discard(possible[j])
    return len(result)