# Lv2 괄호 변환
# 분리
def split(text):
    count = 0
    for i in range(len(text)):
        if text[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return text[:i+1], text[i+1:]
# 올바른 문자열 확인
def allright(text):
    count = 0
    for x in text:
        if x == ")":
            count -= 1
            if count < 0:
                return False
        else:
            count += 1
    return True
# 뒤집기
def reverse(u):
    return ''.join(list(map(lambda x: "(" if x == ")" else ")", u)))
# module
def solution(p):
    # step1
    if p == "":
        return p
    # step2
    u, v = split(p)
    # step3
    if allright(u):
        return u + solution(v)
    # step4
    else:
        return "(" + solution(v) + ")" + reverse(u[1:-1])