# JadenCase 문자열 만들기
def solution(s):
    result = ""
    elem_ls = s.lower().split(" ")
    elem_sz = len(elem_ls)
    for i, elem in enumerate(elem_ls):
        elem = elem.capitalize()
        if i == elem_sz - 1:
            result += elem
        else:
            result += elem + " "
    return result