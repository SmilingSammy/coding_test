# Lv1 음양 더하기
def solution(absolutes, signs):
    result = 0
    for val, sign in zip(absolutes, signs):
        if sign:
            result += val
        else:
            result -= val

    return result