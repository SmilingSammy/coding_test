# 유클리드 호제법
def gcd(a, b):
    if a > b:
        r = a % b
    else:
        r = b % a

    if r == 0:
        return min(a, b)
    else:
        return gcd(min(a, b), r)


def solution(w, h):
    return w * h - (w + h - gcd(w, h))