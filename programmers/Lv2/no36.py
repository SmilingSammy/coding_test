# Lv2 n진수 게임

# n진수 변환
def convert(num, n):
    case = "0123456789ABCDEF"
    q, r = divmod(num, n)
    if q == 0:
        return case[r]
    else:
        return convert(q, n) + case[r]


def solution(n, t, m, p):
    # 최종 튜브가 말해야하는 숫자
    result = ''
    elem_ls = []

    for i in range(t * m):
        value = convert(i, n)

        for elem in value:
            elem_ls.append(elem)

    for order in range(p - 1, t * m, m):
        result += elem_ls[order]

    return result