# 이진 변환 반복하기

def solution(s):
    trans_count = 0
    zero_count = 0

    while s != '1':
        size = s.count("1")
        zero_count += s.count("0")
        s = bin(size)[2:]
        trans_count += 1

    return [trans_count, zero_count]
