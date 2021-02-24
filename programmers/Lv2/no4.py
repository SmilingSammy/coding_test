# 행렬의 곱셈
def solution(arr1, arr2):
    answer = []
    arr2_val = [elem for elem in zip(*arr2)]

    for elem1 in arr1:
        ans_tmp = []
        for elem2 in arr2_val:
            mat_mul = sum(list(map(lambda x:  x[0] * x[1], zip(elem1, elem2))))
            ans_tmp.append(mat_mul)

        answer.append(ans_tmp)
    return answer