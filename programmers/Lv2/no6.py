# 최댓값과 최솟값
def solution(s):
    sort_ls = sorted(list(map(int, s.split())))
    return "{0} {1}".format(sort_ls[0], sort_ls[-1])
