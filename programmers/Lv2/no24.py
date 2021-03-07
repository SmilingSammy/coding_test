# 점프와 순간 이동
def solution(n):
    # 현재 state
    state = 0
    while n != 0:
        n, step = divmod(n, 2)
        state += step
    return state