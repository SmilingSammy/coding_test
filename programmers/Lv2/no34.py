# Lv2 괄호 회전하기

def check_bracket(x):
    open_bracket = ['(', '{', '[']
    close_bracket = [')', '}', ']']
    stack = []

    for elem in x:
        if elem in open_bracket:
            stack.append(elem)
        else:
            if len(stack) == 0:
                return 0
            elif stack[-1] == open_bracket[close_bracket.index(elem)]:
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


def solution(s):
    # 가능한 회전 수
    rotate_count = len(list(s))
    # 올바른 문자열 개수
    correct_count = 0

    for n in range(rotate_count):
        # 문자 회전
        x = s[n:] + s[:n]
        # 올바른 문자열 count
        correct_count += check_bracket(x)

    return correct_count
