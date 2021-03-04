# 예상 대진표
import math
def solution(n, a, b):
    answer = 0
    while(not a==b):
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1
    return answer