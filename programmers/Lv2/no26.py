# 메뉴 리뉴얼
from itertools import combinations
from collections import Counter
def solution(orders, course):
    result = []
    for num in course:
        case = []
        for od in orders:
            od = sorted(list(od))
            case.extend(combinations(od, num))
        case_dict = Counter(case)
        if case_dict:
            max_val = max(case_dict.values())
            if max_val >= 2:
                max_case = [''.join(sorted(list(key))) for key, val in case_dict.items() if val == max_val]
                result += max_case
    result.sort()
    return result