# 구명보트
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q = deque(people)
    while q:
        temp = q.popleft()
        if q and q[-1] <= limit-temp:
            q.pop()
        answer += 1
    return answer