# 짝지어 제거하기
def solution(s):
    s = list(s)
    stack = [s[0]]
    for elem in s[1:]:
        stack.append(elem)

        while len(stack) >=2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()

    return 1 if len(stack) == 0 else 0