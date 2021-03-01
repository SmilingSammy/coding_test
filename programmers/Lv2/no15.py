# [1차 뉴스클러스터링]
import re
import math
from collections import Counter


def solution(str1, str2):
    # 대문자 통일
    str1 = str1.upper()
    str2 = str2.upper()
    # 2글자씩 묶기, 대문자 2개 조합 찾기
    rgx = re.compile("[A-Z]{2}")
    pos_ls1 = [str1[i:i + 2] for i in range(len(str1) - 1) if rgx.findall(str1[i:i + 2])]
    pos_ls2 = [str2[i:i + 2] for i in range(len(str2) - 1) if rgx.findall(str2[i:i + 2])]
    # key: elem
    pos_dict1 = Counter(pos_ls1)
    pos_dict2 = Counter(pos_ls2)
    # 자카드 유사도
    common_sz = 0
    for key in pos_dict1:
        if key in pos_dict2:
            common_sz += min(pos_dict1[key], pos_dict2[key])

    tot_sz = sum(pos_dict1.values()) + sum(pos_dict2.values()) - common_sz

    if tot_sz == 0:
        return 65536
    else:
        return math.trunc(common_sz / tot_sz * 65536)