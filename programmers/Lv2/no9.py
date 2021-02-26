# 튜플
def solution(s):
    # {, } 정제
    s_refine = s[2:-2].split("},{")
    # elemnt 길이 순서로 정렬
    s_sort = sorted(s_refine, key=lambda x: len(x))
    # , 기준 분리 배열 생성
    s_ls = [elem.split(',') for elem in s_sort]

    # 가장 길이가 작은 값 초기 값으로 선정
    result = s_ls[0]

    # 차집합으로 요소 추가
    for x in s_ls[1:]:
        result += list(set(x) - set(result))

    return [int(i) for i in result]