# 최솟값 만들기
def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    s=0
    for i in range(len(A)):
        s += A[i]*B[i]
    return s