# [1차] 캐시
from collections import deque
def solution(cacheSize, cities):
    # 1. 캐시 저장하는 cache deque 자료형 생성
    cache = deque(maxlen=cacheSize)
    # 2. 실행시간 a 생성, cities 반복, lru 캐시처리
    a = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            a += 1
            cache.remove(city)
        else:
            a += 5
        cache.append(city)
    # 3. a 리턴
    return a
