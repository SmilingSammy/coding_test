# 숫자의 표현
## 홀수의 약수 계산

def solution(n):
    res = [i for i in range(1, n + 1, 2) if n % i == 0]

    return len(res)
