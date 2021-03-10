# Lv2 소수 찾기
from itertools import permutations
def prime_num(x):
    for i in range(2, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            return 0
    return 1
def solution(numbers):
    nums = list(numbers)
    case = set()
    for i in range(1, len(nums)+1):
        tmp = []
        tmp.extend(permutations(nums, i))
        tmp = [int(''.join(x)) for x in tmp]
        case |= set(tmp)
    count = 0
    for elem in case:
        if elem < 2:
            continue
        count += prime_num(elem)
    return count