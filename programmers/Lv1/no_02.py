# 소수 만들기 (Lv1)
from itertools import combinations
def solution(nums):
    count = 0
    cases = []
    cases.extend(combinations(nums, 3))
    for case in cases:
        val = sum(case)
        count += 1
        for i in range(2, int(pow(val, 0.5)) + 1):
            if val % i == 0:
                count -= 1
                break
    return count